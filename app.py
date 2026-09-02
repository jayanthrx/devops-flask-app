import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Database configuration (PostgreSQL in production/Docker, SQLite fallback for tests)
db_url = os.environ.get("DATABASE_URL", "sqlite:///app.db")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
metrics = PrometheusMetrics(app)


# Database Model
class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Hello! My DevOps Flask Application is Running."


@app.route("/health")
def health():
    return "Application is healthy!"


@app.route("/api/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200


@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json() or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    item = Item(title=title)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": f"Item {item_id} deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

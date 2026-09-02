import unittest

from app import app, db


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "Hello! My DevOps Flask Application is Running.",
        )

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Application is healthy!")

    def test_metrics_endpoint(self):
        response = self.client.get("/metrics")

        self.assertEqual(response.status_code, 200)
        self.assertIn("flask_http_request_duration_seconds", response.get_data(as_text=True))

    def test_get_items_empty(self):
        response = self.client.get("/api/items")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_create_item_success(self):
        response = self.client.post("/api/items", json={"title": "DevOps Task"})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["title"], "DevOps Task")
        self.assertIn("id", data)

    def test_create_item_missing_title(self):
        response = self.client.post("/api/items", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_delete_item_success(self):
        create_res = self.client.post("/api/items", json={"title": "To Delete"})
        item_id = create_res.get_json()["id"]

        del_res = self.client.delete(f"/api/items/{item_id}")
        self.assertEqual(del_res.status_code, 200)
        self.assertIn("deleted successfully", del_res.get_json()["message"])

    def test_delete_item_not_found(self):
        del_res = self.client.delete("/api/items/99999")
        self.assertEqual(del_res.status_code, 404)
        self.assertIn("Item not found", del_res.get_json()["error"])


if __name__ == "__main__":
    unittest.main()

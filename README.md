# DevOps Flask Application 🚀

A complete end-to-end DevOps pipeline for a Python Flask web application, featuring automated testing, Docker containerization, GitHub Actions CI/CD to Docker Hub, and Kubernetes deployment configurations.

---

## 📋 Architecture & Tech Stack

- **Application**: Python 3.11, Flask
- **Testing**: `unittest`
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Container Registry**: Docker Hub
- **Orchestration**: Kubernetes (Deployment & Service manifests)

---

## 🛠️ Getting Started Locally

### 1. Run with Python Virtual Environment
```bash
# Activate virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run unit tests
python -m unittest discover -v

# Start Flask server
python app.py
```
App will be running at `http://localhost:5000` (`/` and `/health`).

---

### 2. Run with Docker
```bash
# Build Docker image
docker build -t devops-flask-app .

# Run Docker container
docker run -d -p 5000:5000 --name flask-app devops-flask-app
```

---

### 3. Run with Docker Compose
```bash
docker compose up -d --build
```
Stop with:
```bash
docker compose down
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

On every `push` to the `main` branch, the pipeline (`.github/workflows/ci.yml`):
1. Checks out the code.
2. Sets up Python 3.11 environment.
3. Installs requirements.
4. Executes unit tests (`unittest`).
5. Authenticates with Docker Hub using repository secrets (`DOCKERHUB_JAY` and `DOCKER_PASSWORD`).
6. Builds the Docker image.
7. Pushes the image to Docker Hub as `latest`.

---

## ☸️ Kubernetes Deployment

Deploy the application to any Kubernetes cluster (Minikube, Kind, EKS, AKS, GKE):

```bash
# Apply deployment & service manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify pods and service
kubectl get pods -l app=devops-flask-app
kubectl get svc devops-flask-service
```

# DevOps Flask Application 🚀

A production-ready, end-to-end DevOps pipeline for a Python Flask application featuring automated testing, linting, security scanning, Docker containerization, GitHub Actions CI/CD to Docker Hub, Kubernetes manifests, Helm packaging, and Prometheus observability.

---

## 📋 Architecture & Tech Stack

- **Application**: Python 3.11, Flask
- **Observability**: `prometheus-flask-exporter` (exposing `/metrics`)
- **Code Quality & Linting**: `flake8`
- **Testing**: `unittest`
- **Security Scanning**: Aqua Security `Trivy`
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Registry**: Docker Hub
- **Orchestration**: Kubernetes (`k8s/`) & Helm (`helm/devops-flask-app`)

---

## 🌐 Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Application welcome message |
| `/health` | `GET` | Health check probe endpoint (status 200) |
| `/metrics` | `GET` | Prometheus metrics (request count, latency, error rates) |

---

## 🛠️ Getting Started Locally

### 1. Run with Python Virtual Environment
```bash
# Activate virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run linter
flake8 . --max-line-length=100 --exclude=venv,__pycache__

# Run unit tests
python -m unittest discover -v

# Start Flask server
python app.py
```
App will be running at `http://localhost:5000`.

---

### 2. Run with Docker Compose
```bash
docker compose up -d --build
```
Access `http://localhost:5000` or `http://localhost:5000/metrics`.

To stop:
```bash
docker compose down
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

On every `push` to `main`, the workflow (`.github/workflows/ci.yml`):
1. **Checks out code** and configures Python 3.11.
2. **Installs dependencies** including `flake8` and `requirements.txt`.
3. **Lints code** with `flake8` to enforce style and catch errors.
4. **Runs unit tests** via `unittest`.
5. **Authenticates** with Docker Hub using repository secrets (`DOCKERHUB_JAY` and `DOCKER_PASSWORD`).
6. **Builds the Docker container image**.
7. **Scans the image for vulnerabilities** using **Aqua Security Trivy**.
8. **Pushes the image** to Docker Hub as `latest`.

---

## ☸️ Kubernetes Deployment

### Option A: Using Raw Manifests (`k8s/`)
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check pods & service status
kubectl get pods -l app=devops-flask-app
kubectl get svc devops-flask-service
```

### Option B: Using Helm Chart (`helm/`)
```bash
# Install / Upgrade chart
helm upgrade --install devops-flask-app ./helm/devops-flask-app

# Check release status
helm status devops-flask-app

# Uninstall chart
helm uninstall devops-flask-app
```

# DevOps Flask Application 🚀

[![Flask CI/CD](https://github.com/jayanthrx/devops-flask-app/actions/workflows/ci.yml/badge.svg)](https://github.com/jayanthrx/devops-flask-app/actions/workflows/ci.yml)
[![Docker Image](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/r/jayanthrx/devops-flask-app)
[![Python 3.11](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://www.python.org/)
[![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen.svg)](https://github.com/jayanthrx/devops-flask-app)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

A comprehensive, production-grade DevOps repository showcasing end-to-end continuous integration, continuous delivery (CI/CD), infrastructure as code (Terraform), multi-container orchestration with PostgreSQL (Docker Compose & Kubernetes), Helm packaging, and full observability (Prometheus & Grafana).

> 💡 **Preparing for Interviews?** Check out the [**DevOps Portfolio & Interview Guide**](PORTFOLIO_GUIDE.md) for resume bullet points and architectural Q&A.

---

## 📋 Architecture & Tech Stack

- **Application & WSGI**: Python 3.11, Flask, Gunicorn (multi-worker)
- **Database**: PostgreSQL 15 (Docker) / SQLAlchemy ORM
- **Observability**: `prometheus-flask-exporter`, Prometheus, Grafana (Dashboard-as-Code)
- **Code Quality & Testing**: `flake8`, `coverage.py` (97% coverage), `unittest`
- **Security Scanning**: Aqua Security `Trivy` (container vulnerability scanner)
- **Containerization**: Docker, Docker Compose
- **CI/CD Pipeline**: GitHub Actions (Lint $\rightarrow$ Test & Coverage $\rightarrow$ Build $\rightarrow$ Trivy Scan $\rightarrow$ Push $\rightarrow$ Deploy)
- **Registry**: Docker Hub (`jayanthrx/devops-flask-app`)
- **Orchestration**: Kubernetes (`k8s/`) & Helm (`helm/devops-flask-app`)
- **Infrastructure as Code (IaC)**: Terraform (`terraform/` for AWS EC2 + Docker)
- **Cloud Deployment**: Render (`render.yaml`)

---

## 🌐 Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Application welcome message |
| `/health` | `GET` | Health check probe endpoint (status 200) |
| `/metrics` | `GET` | Prometheus metrics (request count, latency, error rates) |
| `/api/items` | `GET` | Retrieve all items from PostgreSQL database |
| `/api/items` | `POST` | Create a new item (`{"title": "My Task"}`) |
| `/api/items/<id>` | `DELETE` | Delete an item by ID |

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

# Run unit tests with coverage
coverage run -m unittest discover -v
coverage report -m

# Start Flask server
python app.py
```
App will be running at `http://localhost:5000`.

---

### 2. Run Full Multi-Container Stack with Docker Compose
Spin up the Flask app, PostgreSQL, Prometheus, and Grafana simultaneously:
```bash
docker compose up -d --build
```

**Services Available:**
- 🌐 **Flask App & REST API**: [http://localhost:5000](http://localhost:5000)
- 🗄️ **PostgreSQL Database**: `localhost:5432` (`flask_db`)
- 🔥 **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
- 📊 **Grafana Dashboard**: [http://localhost:3000](http://localhost:3000) *(User: `admin`, Pass: `admin`)*
  - Pre-loaded with the **Flask Application Dashboard** (Total Requests, Rates, p95/p99 Latencies).

To stop all services:
```bash
docker compose down
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

On every `push` to `main`, the workflow (`.github/workflows/ci.yml`):
1. **Linting**: Enforces clean Python style and syntax via `flake8`.
2. **Testing & Coverage**: Runs 8 test cases with `coverage.py` (**97% coverage**).
3. **Docker Hub Login**: Securely authenticates via repository secrets (`DOCKERHUB_JAY` and `DOCKER_PASSWORD`).
4. **Container Build**: Builds Docker container with Gunicorn WSGI.
5. **Security Scan**: Aqua Security `Trivy` scans the image for vulnerabilities.
6. **Docker Push**: Pushes image to Docker Hub as `latest`.
7. **Continuous Deployment**: Triggers deployment verification.

---

## ☸️ Kubernetes & Helm Deployment

### Option A: Raw Kubernetes Manifests (`k8s/`)
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

kubectl get pods -l app=devops-flask-app
kubectl get svc devops-flask-service
```

### Option B: Using Helm Chart (`helm/`)
```bash
helm upgrade --install devops-flask-app ./helm/devops-flask-app
helm status devops-flask-app
```

---

## ☁️ Infrastructure as Code with Terraform

Provision an AWS EC2 instance running Docker with this app pre-deployed:

```bash
cd terraform

# Initialize Terraform plugins
terraform init

# Review execution plan
terraform plan

# Provision infrastructure
terraform apply
```

To tear down cloud resources:
```bash
terraform destroy
```

---

## 🚀 1-Click Free Cloud Deployment (Render)

This repository includes a [`render.yaml`](render.yaml) blueprint:
1. Connect this GitHub repository to [Render.com](https://render.com).
2. Select **New $\rightarrow$ Blueprint**.
3. Render will automatically build the Dockerfile and deploy your app with free HTTPS!

# DevOps Flask Application 🚀

A comprehensive, production-grade DevOps repository showcasing end-to-end continuous integration, continuous delivery (CI/CD), infrastructure as code (Terraform), container orchestration (Docker Compose & Kubernetes), Helm packaging, and full observability (Prometheus & Grafana).

---

## 📋 Architecture & Tech Stack

- **Application**: Python 3.11, Flask, Gunicorn WSGI Server (multi-worker)
- **Observability**: `prometheus-flask-exporter`, Prometheus, Grafana
- **Code Quality & Linting**: `flake8`
- **Testing**: `unittest`
- **Security Scanning**: Aqua Security `Trivy` (vulnerability scanner)
- **Containerization**: Docker, Docker Compose
- **CI/CD Pipeline**: GitHub Actions (Lint $\rightarrow$ Test $\rightarrow$ Build $\rightarrow$ Trivy Scan $\rightarrow$ Push $\rightarrow$ Deploy)
- **Registry**: Docker Hub (`jayanthrx/devops-flask-app`)
- **Orchestration**: Kubernetes (`k8s/`) & Helm (`helm/devops-flask-app`)
- **Infrastructure as Code (IaC)**: Terraform (`terraform/` for AWS EC2 + Docker)

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

# Start Flask server with Gunicorn (or python app.py on Windows)
python app.py
```
App will be running at `http://localhost:5000`.

---

### 2. Run Full Observability Stack with Docker Compose
Spin up the Flask app, Prometheus, and Grafana simultaneously:
```bash
docker compose up -d --build
```

**Services Available:**
- 🌐 **Flask App**: [http://localhost:5000](http://localhost:5000)
- 🔥 **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
- 📊 **Grafana Dashboard**: [http://localhost:3000](http://localhost:3000) *(User: `admin`, Pass: `admin`)*

To stop all services:
```bash
docker compose down
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

On every `push` to `main`, the workflow (`.github/workflows/ci.yml`):
1. **Linting**: Enforces clean Python style and syntax via `flake8`.
2. **Testing**: Runs automated test suite using `unittest`.
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

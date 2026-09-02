# 💼 DevOps Engineer Portfolio & Interview Guide

This guide summarizes the architectural decisions, tools, and key achievements of this project for your **Resume**, **LinkedIn**, and **Technical Job Interviews**.

---

## 📄 Resume Bullet Points (Ready to Copy/Paste)

### **DevOps Engineer / Cloud Engineer Project Experience**

- **Enterprise CI/CD Automation**: Engineered a zero-downtime GitHub Actions CI/CD pipeline enforcing automated linting (`flake8`), unit testing with **97% code coverage** (`coverage.py`), and **Aqua Security Trivy** vulnerability scanning.
- **Production Containerization & WSGI**: Containerized Python Flask services using multi-stage Docker builds with **Gunicorn WSGI** (multi-worker configuration) and optimized build context via `.dockerignore`.
- **Full-Stack Observability**: Architected a real-time observability platform integrating **Prometheus** custom metrics scraping with **Grafana Dashboard-as-Code** provisioning for tracking throughput, HTTP response codes, and p95/p99 request latencies.
- **Multi-Container Orchestration**: Configured multi-tier **Docker Compose** orchestration linking PostgreSQL database (with custom health checks and persistent volumes), Flask application, Prometheus, and Grafana.
- **Cloud-Native Orchestration & Helm**: Authored **Kubernetes (K8s)** manifests featuring liveness/readiness health probes, CPU/memory resource limits, NodePort routing, and packaged customizable **Helm Charts** for multi-environment deployments.
- **Infrastructure as Code (IaC)**: Automated cloud infrastructure provisioning using **Terraform** to deploy AWS EC2 instances, Security Groups, and automated container bootstrapping via cloud-init user data scripts.
- **1-Click Cloud Deployment**: Integrated **Render Blueprint** infrastructure-as-code for automated zero-configuration cloud hosting with automated TLS/SSL.

---

## 🎯 Key Technical Interview Q&A

### 1. *Why did you use Gunicorn instead of Flask's built-in `app.run()`?*
> **Answer**: Flask's built-in development server is single-threaded and not designed for production concurrency or security. Gunicorn acts as a production WSGI HTTP server using a master-worker process model. In our Dockerfile (`gunicorn -w 4 -b 0.0.0.0:5000 app:app`), Gunicorn spawns 4 worker processes capable of handling concurrent incoming web requests without blocking.

### 2. *How does your CI/CD security pipeline work?*
> **Answer**: Every code push to the `main` branch undergoes automated quality and security gates in GitHub Actions:
> 1. Static code analysis & style enforcement via `flake8`.
> 2. Automated test execution and code coverage reporting using `unittest` and `coverage.py`.
> 3. Multi-layer Docker build with secure registry authentication via GitHub Secrets.
> 4. Automated container image CVE vulnerability scanning with **Aqua Security Trivy** filtering for CRITICAL and HIGH severity issues before any image is pushed to Docker Hub.

### 3. *How is observability implemented?*
> **Answer**: Observability is built on three pillars:
> - **Instrumentation**: The Flask app uses `prometheus-flask-exporter` to expose latency histograms, request counters, and HTTP status distributions at `/metrics`.
> - **Metrics Collection**: Prometheus scrapes the `/metrics` endpoint on a 5-second interval.
> - **Visualization (Dashboard-as-Code)**: Grafana is provisioned using YAML configuration files (`provisioning/datasources` and `provisioning/dashboards`) to automatically display pre-configured p95/p99 latency timeseries, request volume, and error rates upon container startup.

### 4. *Why did you package the Kubernetes manifests as a Helm Chart?*
> **Answer**: Plain YAML manifests can become brittle and difficult to manage across multiple environments (e.g., Development, Staging, Production). Helm enables parameterization of image tags, replica counts, and resource limits inside `values.yaml`, making deployments modular, versioned, and easy to rollback with `helm rollback`.

### 5. *How is database persistence handled in Docker Compose?*
> **Answer**: PostgreSQL runs in an isolated container configured with a named Docker volume (`postgres_data:/var/lib/postgresql/data`) to ensure database records persist across container restarts or upgrades. Additionally, Docker health checks (`pg_isready`) ensure the Flask application waits until PostgreSQL is accepting connections before starting.

---

## 🛠️ Complete Technology Matrix

| Category | Technologies Used |
| :--- | :--- |
| **Backend & WSGI** | Python 3.11, Flask 3.1, Gunicorn, SQLAlchemy, Psycopg2 |
| **Database** | PostgreSQL 15, SQLite (test fallback) |
| **Quality & Testing** | Python `unittest`, `coverage.py` (97%), `flake8` |
| **Containers & Orchestration** | Docker, Docker Compose, Kubernetes (K8s), Helm |
| **CI/CD & Security** | GitHub Actions, Aqua Security Trivy, Docker Hub |
| **Observability** | Prometheus, Grafana (Dashboard-as-Code) |
| **Infrastructure as Code** | Terraform (AWS EC2, VPC Security Groups), Render Blueprint |

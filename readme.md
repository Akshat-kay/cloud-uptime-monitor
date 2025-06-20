# 🛠️ Cloud Uptime Monitor (SRE Project)

This is a cloud-native uptime monitoring project for [https://www.loblaw.ca](https://www.loblaw.ca), developed to demonstrate skills relevant to a Site Reliability Engineer (SRE) role at Loblaw Companies Ltd.

## 🔍 What It Does

- Periodically checks the availability of https://www.loblaw.ca
- Exposes real-time metrics via `/metrics` in Prometheus format
- Deploys as a Dockerized app to a Google Kubernetes Engine (GKE) cluster
- Uses Cloud Build for continuous integration and deployment
- Integrates with Cloud Monitoring for alerting and observability

## 🚀 Stack

- Python (Flask)
- Docker
- Kubernetes (GKE)
- Google Cloud Build (CI/CD)
- Cloud Monitoring + Alerting
- Prometheus-compatible metric endpoint

## 📊 Live Metric Example

Visit: `http://<external-ip>/metrics`

Output:

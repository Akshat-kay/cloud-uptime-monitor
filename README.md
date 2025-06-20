# 🛠️ Cloud Uptime Monitor for Loblaw.ca

This is a cloud-native uptime monitoring system built specifically to demonstrate platform reliability and observability for the **Site Reliability Engineer I (Platform Engineering)** role at **Loblaw Companies Ltd.**

<p align="center">
  <img src="docs/architecture.png" width="600" alt="Architecture Diagram">
</p>

---

## 🔍 What It Does

- Periodically checks the availability of **https://www.loblaw.ca**
- Exposes a Prometheus-compatible metric: `uptime_loblaw_status` on `/metrics`
- Sends alerts via **Google Cloud Monitoring** if the site becomes unreachable
- Deploys via CI/CD pipeline using **Cloud Build → GKE**

---

## 🛠️ Tech Stack

- **Python + Flask** – app logic and metric endpoint
- **Docker** – containerization
- **Google Kubernetes Engine (GKE)** – scalable deployment
- **Google Cloud Build** – CI/CD automation
- **Cloud Monitoring + Alerting** – observability and reliability

---

## 🌐 Live Demo URLs (after deploy)

- App: `http://<EXTERNAL-IP>/`
- Metrics: `http://<EXTERNAL-IP>/metrics`

Example output:
![checking loblaws](https://github.com/user-attachments/assets/a3d14db0-802d-47c7-b1bd-b60391c1d9b1)

![1st](https://github.com/user-attachments/assets/fd947376-0576-4d30-b7e8-fd194bdacbf6)

![Screenshot (2893)](https://github.com/user-attachments/assets/aeeacb62-1869-4ab8-aa83-617cc844dc26)



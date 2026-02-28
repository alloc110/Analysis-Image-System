# 🏠 Caption image System


![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.27-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-AI-8E75B2?style=for-the-badge&logo=google&logoColor=white)

> **Project:** J-DataPipe Architecture  
> **University:** Ho Chi Minh City Open University  
> **Tech Stack:** Minikube, Helm, Prometheus, Grafana, Gemini API

An intelligent microservices system that leverages **Google's Gemini API** to analyze images, provide architectural reviews, and estimate potential value. The system is containerized with **Docker**, orchestrated using **Kubernetes (Minikube)**, and fully monitored with **Prometheus & Grafana**.

---

## 📋 Table of Contents

- [Repository Structure](#-repository-structure)
- [High-level System Architecture](#-high-level-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [Monitoring & Observability](#-monitoring--observability)
- [Demo Video](#-demo-video)

---

## 📂 Repository Structure

```bash
house-predict-system/
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── worker.py
├── assets
│   ├── image
│   └── video
├── config
│   ├── deployment.yaml
│   ├── fastapi-monitor.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── Dockerfile
├── Jenkinsfile
├── README.md
└── requirements.txt            # Project Documentation
```

## 🏢 High-level System Architecture

![High-level System Architecture](assets/image/architecture.png)

## 🔧 Prerequisites

To run this project locally, ensure you have the following tools installed:

| Tool               | Description                                                                        | Download / Guide                                                 |
| :----------------- | :--------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| **Docker Desktop** | Container runtime required to build images and run Minikube.                       | [Download Here](https://www.docker.com/products/docker-desktop/) |
| **Minikube**       | Runs a single-node Kubernetes cluster on your personal computer.                   | [Installation Guide](https://minikube.sigs.k8s.io/docs/start/)   |
| **Kubectl**        | The Kubernetes command-line tool allows you to run commands against K8s clusters.  | [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)       |
| **Helm**           | The package manager for Kubernetes (Required for installing Prometheus & Grafana). | [Install Helm](https://helm.sh/docs/intro/install/)              |
| **Gemini API Key** | **Required** for the AI to analyze house images.                                   | [Get Free Key](https://aistudio.google.com/)                     |

### ✅ Verification

Run the following commands in your terminal to verify the installation:

```bash
docker --version      # Should be v20.10+
minikube version      # Should be v1.30+
kubectl version --client
helm version
```

## 🕹️ Installation & Setup

### 1. Clone the Repository

Get the source code to your local machine:

```bash
git clone https://github.com/alloc110/Analysis-Image-System.git
cd Analysis-Image-System
```

### 2. Start Minikube

Initialize the local Kubernetes cluster using the Docker driver:

```bash
minikube start --driver=docker
```

### 3. Setup Namespaces

Create isolated environments for the Application and Monitoring tools.

```bash
# Create namespaces
kubectl create namespace default-namespace
kubectl create namespace monitoring-namespace

# Set default context to 'default-namespace'
kubectl config set-context --current --namespace=default-namespace
```

### 4. Configure Secrets

Replace YOUR_API with your actual key from Google AI Studio.

```bash
kubectl create secret generic gemini-secret \
  --from-literal=GEMINI_API_KEY=YOUR_API \
  -n default-namespace
```

### 5.Deploy the Application

Apply the manifest files to create the Deployment (Pods) and Service (Networking):

```bash
kubectl apply -f config/deployment.yaml
kubectl apply -f config/service.yaml
```

## 🎮 Running the Application

### 1. Port Forwarding

Open a new terminal window and run the following command to create a tunnel from your machine to the Kubernetes cluster:

```bash
kubectl port-forward svc/fastapi-service 8000:80 -n default-namespace
# Keep this terminal open while you use the app
```

### 2. Access the Interface

Once the port-forward is running, access the FastAPI Swagger UI by clicking the link below:

👉 http://localhost:8000/docs

## 🖥️ Monitoring & Observability

We use **Prometheus** to scrape metrics and **Grafana** to visualize them. Ensure you have **Helm** installed.

### 1. Install Prometheus Stack

Add the community repository and install the stack into the `monitoring-namespace` namespace:

```bash
# Add Helm Repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install the Stack
helm install monitor-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring-namespace
```

### 2.Configure Service Monitor

Tell Prometheus to scrape metrics from our FastAPI application:

```bash
kubectl apply -f config/fastapi-monitor.yaml -n monitoring-namespace
```

### 3. Access Grafana Dashboard

To view the metrics, you need to retrieve the admin password and forward the port.

**Step 1**: Get the Admin Password Run this command to decode the default password:

```bash
kubectl get secret --namespace monitoring-namespace monitor-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
# Copy the output string, you will need it to login
```

**Step 2**: Port-forward Grafana Open a new terminal and run:

```bash
kubectl port-forward svc/monitor-stack-grafana 3000:80 -n monitoring-namespace
```

**Step 3**: Login

👉 URL: http://localhost:3000

User: admin

Password: (Paste the password from Step 1)
Import Dashboard ID 12900 in Grafana.

## ⚓ Demo Video

### Demo FastAPI

![🎥 Xem Demo Video](assets/video/video_demo_fastapi.gif)

### Demo Grafana

![🎥 Xem Demo Video](assets/video/video_demo_grafana.gif)

# 🏠 AI House Reviewer & Price Prediction System

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.27-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-AI-8E75B2?style=for-the-badge&logo=google&logoColor=white)

> **Project:** J-DataPipe Architecture  
> **University:** Ho Chi Minh City Open University  
> **Tech Stack:** Minikube, Helm, Prometheus, Grafana, Gemini API

An intelligent microservices system that leverages **Google's Gemini API** to analyze house images, provide architectural reviews, and estimate potential value. The system is containerized with **Docker**, orchestrated using **Kubernetes (Minikube)**, and fully monitored with **Prometheus & Grafana**.

---

## 📋 Table of Contents

- [Repository Structure](#-repository-structure)
- [High-level System Architecture](#-high-level-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [Monitoring & Observability](#-monitoring--observability)
- [Troubleshooting](#-troubleshooting)
- [Demo Video](#-demo-video)

---

## 📂 Repository Structure

```bash
house-predict-system/
├── app/                        # Application Source Code
│   ├── main.py                 # FastAPI backend & Gemini logic
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Instructions to build the Image
├── k8s/                        # Infrastructure as Code (YAML)
│   ├── namespaces.yaml         # Namespace definitions
│   ├── deployment.yaml         # App deployment (Replicas, Resources)
│   ├── service.yaml            # Network exposure (NodePort)
│   └── ingress.yaml            # Nginx Ingress rules
├── monitoring/                 # Monitoring Configurations
│   └── fastapi-monitor.yaml    # ServiceMonitor for Prometheus
└── README.md                   # Project Documentation
```

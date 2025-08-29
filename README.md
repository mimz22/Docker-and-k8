# Dockerized Microservices with Kubernetes

## Overview

This project demonstrates a **Dockerized microservices architecture** deployed on **Kubernetes**. It showcases a full-stack system with three interconnected services:


- **Frontend Service**: Serves the user interface.
 
- **User Service**: Handles user data and API requests.
 
- **Payment Service**: Handles mock payment processing.

All services are containerized with **Docker** and orchestrated on **Kubernetes (Minikube)**.

---

## Architecture

[Frontend Service]

--> [User Service]

--> [Payment Service]


- Each service runs in its **own container**.

- Services communicate internally via **Kubernetes service DNS**.

- The frontend exposes a **NodePort** to access the application from the browser.

---

## Tech Stack & Skills Highlighted

- **Docker**: Containerized all services for consistency and portability.

- **Kubernetes**: Orchestrated containers using Deployments, Services, and NodePorts.

- **Minikube**: Local Kubernetes cluster for development and testing.

- **Microservices Architecture**: Decoupled services with independent deployments.

- **Networking in Kubernetes**: Internal service communication and external exposure via NodePort.

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)

- [Minikube](https://minikube.sigs.k8s.io/docs/)

- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

---

### Steps to Run Locally

1. **Clone the repository**:


git clone https://github.com/Sam6569/docker-k8s-microservices.git

cd k8s-microservices


Start Minikube:

minikube start


Apply Kubernetes configurations:

kubectl apply -f k8s-all.yaml


Check pods status:

kubectl get pods


Access the frontend service:

minikube service frontend-service --url


Open the URL in your browser. You should see the frontend connecting to user and payment services.

Testing Internal Connectivity

If needed, test service-to-service communication from within the cluster:

kubectl exec -it <frontend-pod-name> -- curl http://user-service

kubectl exec -it <frontend-pod-name> -- curl http://payment-service


(Make sure curl is installed in the container)

Project Structure

k8s-microservices/
│
├─ frontend-service/      # Frontend code & Dockerfile

├─ user-service/          # User API & Dockerfile

├─ payment-service/       # Payment API & Dockerfile

├─ k8s-all.yaml           # Kubernetes deployments & services

├─ README.md

Notes

Frontend handles backend errors gracefully, showing "Service unavailable" if backend services are not ready.

You can extend this project by adding CI/CD, monitoring, or cloud deployment (EKS/GKE/AKS).




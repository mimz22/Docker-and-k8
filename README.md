# Kubernetes Microservices Demo

A simple microservices architecture built with Flask and deployed on Kubernetes, demonstrating service-to-service communication and container orchestration.

## Architecture

This project consists of three microservices:

- **Frontend Service** - Main entry point that aggregates data from other services
- **User Service** - Provides user information
- **Payment Service** - Handles payment processing

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Frontend       │───▶│  User Service   │    │ Payment Service │
│  Service        │    │                 │    │                 │
│  (Port 5000)    │───▶│  (Port 5000)    │    │  (Port 5000)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Services

### Frontend Service
- **Endpoint**: `/`
- **Function**: Aggregates responses from user and payment services
- **Dependencies**: Flask, Requests

### User Service
- **Endpoint**: `/user`
- **Function**: Returns user information (ID, name, status)
- **Dependencies**: Flask

### Payment Service
- **Endpoint**: `/payment`
- **Function**: Returns payment details (ID, amount, currency, status)
- **Dependencies**: Flask

## Prerequisites

- Docker
- Kubernetes cluster (minikube, Docker Desktop, or cloud provider)
- kubectl configured

## Quick Start

### 1. Deploy to Kubernetes

```bash
kubectl apply -f k8s-all.yaml
```

### 2. Access the Application

Get the NodePort for the frontend service:
```bash
kubectl get services frontend-service
```

Access the application at `http://localhost:<NodePort>` or `http://<cluster-ip>:<NodePort>`

### 3. Test the Services

The frontend service will return a JSON response containing data from all three services:

```json
{
  "frontend": "hello from frontend-service",
  "user": {
    "id": 1,
    "name": "Samuel",
    "status": "active"
  },
  "payment": {
    "payment_id": 101,
    "amount": "50.00",
    "currency": "USD",
    "status": "success"
  }
}
```

## Development

### Local Development

Each service can be run locally:

```bash
cd frontend-service
pip install -r requirements.txt
python app.py
```

### Building Docker Images

Build images for each service:

```bash
# User Service
cd user-service
docker build -t sam6569/user-service:1.0 .

# Payment Service
cd payment-service
docker build -t sam6569/payment-service:1.0 .

# Frontend Service
cd frontend-service
docker build -t sam6569/frontend-service:1.0 .
```

### Push to Registry

```bash
docker push sam6569/user-service:1.0
docker push sam6569/payment-service:1.0
docker push sam6569/frontend-service:1.0
```

## Kubernetes Configuration

The `k8s-all.yaml` file contains:
- Deployments for each service (2 replicas each)
- ClusterIP services for internal communication
- NodePort service for external access to frontend

## Cleanup

Remove all resources:

```bash
kubectl delete -f k8s-all.yaml
```

## Features

- **Service Discovery**: Services communicate using Kubernetes DNS
- **High Availability**: 2 replicas per service
- **Fault Tolerance**: Frontend handles service unavailability gracefully
- **Container Orchestration**: Full Kubernetes deployment configuration
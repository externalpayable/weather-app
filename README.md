# Flask Weather App

This is a simple Flask weather app that fetches weather information from the OpenWeatherMap API based on the provided city name.

## Containerization and Deployment

This project utilizes containerization tools like Docker and Kubernetes to package and deploy the Flask weather app consistently across different environments.

### Docker

To run the Flask weather app using Docker, follow the steps below:

1. Make sure you have Docker installed on your machine.

2. Clone the repository:

```bash
git clone https://github.com/kd9s0/app-containerization.git
cd app-containerization
```

3. Build the Docker Image
```
docker build -t app-containerization .
```

4. Run the Docker Container
```
docker run -d -p 5000:5000 app-containerization
```

5. Open your web browser and access the app at http://localhost:5000/weather/<city>, where <city> is the desired city name for weather information.

## Kubernetes

To deploy the Flask weather app using Kubernetes, follow the steps below:

1. Make sure you have a Kubernetes cluster set up (e.g., minikube, Docker Desktop with Kubernetes, or a cloud-based cluster).

2. Clone the repository

```bash
git clone https://github.com/kd9s0/app-containerization.git
cd app-containerization
```

3. Deploy the app to kubernetes

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

4. Get the external IP of the service
```
kubectl get services
```

5. Open your web browser and access the app at http://<external_ip>/weather/<city>, where <external_ip> is the external IP of the service and <city> is the desired city name for weather information.
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
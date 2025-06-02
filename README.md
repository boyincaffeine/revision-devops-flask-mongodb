# Revision Project: DevOps with Flask & MongoDB

This repository contains a simple Flask application connected to MongoDB, containerized using Docker and orchestrated with Docker Compose.  
It serves as a hands-on revision project for core DevOps concepts including containerization, multi-service orchestration, and app deployment basics.

---

## Project Structure

- `app.py` — Flask application connecting to MongoDB
- `Dockerfile` — Docker image build instructions for the Flask app
- `docker-compose.yml` — Defines two services: `web` (Flask app) and `rev` (MongoDB)
- `requirement.txt` — Python dependencies for the Flask app

---

## How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/revision-devops-flask-mongodb.git
   cd revision-devops-flask-mongodb
Build and start services:

bash
Copy
Edit
docker-compose up --build
Access the app:

Open your browser and go to http://localhost:5000

What Happens
The Flask app starts on port 5000

The MongoDB service starts on port 27017

The Flask app connects to MongoDB using the service name rev

On visiting /, the app inserts a sample document into MongoDB

Troubleshooting
Ensure Docker and Docker Compose are installed

If MongoDB connection errors occur, confirm the MongoClient URI in app.py uses mongodb://rev:27017

Rebuild containers if code changes:

bash
Copy
Edit
docker-compose down
docker-compose up --build
Author
Sahil Verma
GitHub | LinkedIn

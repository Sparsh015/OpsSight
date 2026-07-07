
# OpsSight - API Monitoring System

OpsSight is a backend API monitoring platform built using FastAPI.  
It allows users to monitor APIs, automatically perform health checks, track response times, detect failures, and manage incidents.

## 🚀 Live Demo

API Base URL:

https://opssight.onrender.com

Swagger Documentation:

https://your-render-url.onrender.com/docs

## Features

- User authentication using JWT
- Secure password hashing
- Create and manage API monitors
- Automated API health checks
- Background scheduling using APScheduler
- Response time tracking
- Check history storage
- Automatic incident detection
- Duplicate incident prevention
- Incident auto-resolution
- Dashboard analytics
- Application logging

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- APScheduler
- HTTPX
- Python Logging

## System Architecture

```
User
 |
 v
FastAPI Routes
 |
 v
Services Layer
 |
 +----------------+
 |                |
Monitor Checks   Incident Handler
 |
 v
PostgreSQL Database
```

## Database Models

### User

Stores user authentication details.

### Monitor

Stores APIs being monitored.

Fields include:

- URL
- HTTP method
- Check interval
- Timeout
- Latency threshold

### CheckResult

Stores every health check result:

- Status code
- Response time
- Success/failure status
- Error details

### Incident

Stores API issues:

- Failure message
- Severity
- Resolution status


## Main API Endpoints

### Authentication

```
POST /register
POST /login
```

### Monitors

```
POST /monitors
GET /monitors
PUT /monitors/{id}
DELETE /monitors/{id}
```

### Health Checks

```
POST /monitors/{id}/check

GET /monitors/{id}/results
```

### Incidents

```
GET /incidents
```

### Dashboard

```
GET /dashboard
```

## How Monitoring Works

```
Scheduler runs
        |
        v
Fetch active monitors
        |
        v
Check if interval passed
        |
        v
Send HTTP request
        |
        v
Save CheckResult
        |
        v
Detect Incident
```

## Incident Flow

```
API Failure
     |
     v
Check existing active incident

     |
+----+----+
|         |
Exists    No Incident
|         |
Ignore    Create Incident


When API recovers

Resolve Incident
```

## Setup Instructions

Clone repository

```bash
git clone <repo-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment file

```
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
```

Run server

```bash
uvicorn app.main:app --reload
```

## Future Improvements

- Async API checks
- Email notifications
- Docker support
- Redis queue system
- Advanced monitoring graphs
- CI/CD pipeline

---

Built as a production-style backend monitoring system.

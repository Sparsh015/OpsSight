# OpsSight - API Monitoring System

OpsSight is a backend API monitoring platform built using FastAPI.

It allows users to monitor APIs, automatically perform health checks, track response times, detect failures, manage incidents, and analyze API reliability.

---

## 🚀 Live Demo

API Base URL:

https://opssight.onrender.com

Swagger Documentation:

https://opssight.onrender.com/docs

---

## Features

- User authentication using JWT
- Secure password hashing
- Create and manage API monitors
- Automated API health checks
- Background scheduling using APScheduler
- Configurable monitoring intervals
- Response time tracking
- API check history storage
- Latency threshold monitoring
- Automatic incident detection
- Duplicate incident prevention
- Incident auto-resolution
- Dashboard analytics
- Application logging

---

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
- Render
- Neon PostgreSQL

---

## Deployment

The application is deployed using:

- Render for FastAPI backend hosting
- Neon PostgreSQL for cloud database

Production setup:

```text
GitHub Repository
        |
        v
 Render Web Service
        |
        v
 FastAPI Application
        |
        v
 Neon PostgreSQL
```

---

## System Architecture

```text
                         Client
                           |
                           v
                    FastAPI Application
                    (Render Deployment)

                           |
        -----------------------------------------
        |                    |                  |
        v                    v                  v

 Authentication        Monitor APIs       Dashboard APIs
 (JWT + Hashing)        (CRUD APIs)        (Analytics)


                           |
                           v

                    Service Layer
              (Business Logic Separation)

                           |
        --------------------------------
        |                              |
        v                              v

 Monitor Engine                 Incident Manager

 HTTPX Requests                 Detect Failures
 Response Tracking              Prevent Duplicates
 Latency Checks                 Auto Resolution

                           |
                           v

                 SQLAlchemy ORM Layer

                           |
                           v

              Neon PostgreSQL Database

        users
        monitors
        checkresults
        incidents

                           ^
                           |
                    APScheduler

              Background Health Checks
              Custom Check Intervals
```

---

## Database Models

### User

Stores user authentication details.

Includes:

- Username
- Email
- Hashed password
- User role
- Account timestamps

---

### Monitor

Stores APIs configured for monitoring.

Includes:

- API URL
- HTTP method
- Check interval
- Timeout settings
- Latency threshold
- Active status

---

### CheckResult

Stores every API health check.

Includes:

- HTTP status code
- Response time
- Success/failure status
- Error information
- Check timestamp

---

### Incident

Stores API reliability issues.

Includes:

- Failure message
- Severity level
- Resolution status
- Creation time
- Resolution time

---

## Main API Endpoints

### API Documentation

```http
GET /docs
```

---

### Authentication

```http
POST /register

POST /login
```

---

### Monitors

```http
POST /monitors

GET /monitors

PUT /monitors/{id}

DELETE /monitors/{id}
```

---

### Health Checks

```http
POST /monitors/{id}/check

GET /monitors/{id}/results
```

---

### Incidents

```http
GET /incidents
```

---

### Dashboard

```http
GET /dashboard
```

---

## How Monitoring Works

```text
Scheduler starts

        |
        v

Fetch active monitors

        |
        v

Check monitor interval

        |
        v

Send HTTP request using HTTPX

        |
        v

Measure response time

        |
        v

Save CheckResult

        |
        v

Analyze health status

        |
        v

Create or resolve incidents
```

---

## Incident Flow

```text
API Failure / Slow Response

          |
          v

Check for active incident

          |
   +------+------+
   |             |
   v             v

Exists      No Incident

   |             |

Ignore      Create Incident


When API becomes healthy

          |
          v

Resolve Incident
```

---

## Setup Instructions

Clone repository:

```bash
git clone <repo-url>
```

Move into project:

```bash
cd OpsSight
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
DATABASE_URL=

SECRET_KEY=

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```
---

Built as a production-style backend project demonstrating authentication, monitoring, background processing, database design, and cloud deployment.

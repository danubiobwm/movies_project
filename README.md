# 🎬 Movie Data Pipeline - Backend Challenge

This project is a complete solution to the technical challenge with Django, Celery, MongoDB, RabbitMQ and FastAPI. It integrates data from TheMovieDB, performs synchronizations and exposes REST and reporting APIs.

---

## 🔧 Technologies used

- Django + Django REST Framework
- PostgreSQL + Django ORM
- Celery + RabbitMQ
- MongoDB (reporting)
- FastAPI
- Docker + Docker Compose

---

## 🚀 How to run the project locally

```bash
git clone https://github.com/danubiobwm/movies_project
cd movies_project
cp .env.example .env
docker-compose up --build
```

Access the URLs:
- Django: http://localhost:8000/api/movies/
- FastAPI: http://localhost:9000/docs
- RabbitMQ: http://localhost:15672

---

## 📌 functionality
- Integration with TheMovieDB
- Periodic update with Celery
- Movie CRUD via Django API
- Filters, sorting and pagination
- Synchronization with MongoDB
- FastAPI report endpoints

---

## ✅ Tests

```bash
docker-compose run backend pytest
```

## 🚧 Creation of the project
```
docker-compose run backend django-admin startproject app .
docker-compose run backend python manage.py startapp movies
docker compose up -d --build backend celery celery-beat

```

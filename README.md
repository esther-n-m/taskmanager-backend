# Task Manager API

A simple backend project built with **Django REST Framework (DRF)** for managing tasks.  
This project is part of my Capstone Project.
It lets you create, update, delete, and manage tasks — with authentication, filtering, and API docs powered by Swagger.

---

## Features

Create, read, update, and delete tasks (CRUD).

Token-based authentication.

Mark tasks as complete/incomplete.

Filter tasks by status or due date.

API documentation with Swagger.

---

## Tech Stack

Django 5

Django REST Framework

SQLite (dev database)

---

## Setup

Clone the repo:

git clone https://github.com/esther-n-m/taskmanager-backend.git
cd taskmanager-backend


Create & activate a virtual environment:

python -m venv venv
source venv/Scripts/activate   # Windows


Install dependencies:

pip install -r requirements.txt


Run migrations & start server:

python manage.py migrate
python manage.py runserver

---

## Authentication

Login via: /api-token-auth/

Then include token in headers:

Authorization: Token your_token_here

---

## API Endpoints

GET /api/tasks/ → list tasks

POST /api/tasks/ → create task

GET /api/tasks/{id}/ → task details

PUT/PATCH /api/tasks/{id}/ → update task

DELETE /api/tasks/{id}/ → delete task

POST /api/tasks/{id}/complete/ → mark complete

POST /api/tasks/{id}/incomplete/ → mark incomplete

GET /swagger/ → API docs

---

## Reflection

Building this project helped me deepen my understanding of Django REST Framework, authentication, and API design. It’s a solid foundation for real-world backend development.
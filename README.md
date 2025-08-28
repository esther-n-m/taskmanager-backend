# Task Manager API

A simple backend project built with **Django REST Framework (DRF)** for managing tasks.  
This project is part of my Capstone Project.

---

## Week 1 Progress ✅
- Set up project structure  
- Created and activated virtual environment  
- Installed Django & DRF (listed in `requirements.txt`)  
- Created initial Django project (`taskmanager`) and app (`tasks`)  
- Initialized Git and pushed project to GitHub  

---

## Week 2 Progress ✅
- Implemented **Task CRUD operations**:
  - Create, Read, Update, Delete tasks
  - Each task has:
    - Title
    - Description
    - Due Date
    - Priority Level (Low, Medium, High)
    - Status (Pending, Completed)
- Added **validations**:
  - Due date must be in the future
  - Restrict priority level to allowed choices
- Created **Task serializer, viewset, and routes**
- Registered API endpoints in `urls.py`
- Added database migrations for the Task model
- Added `.gitignore` file to exclude virtual environment, `__pycache__`, `.sqlite3`, etc.

---

## Next Steps (Week 3 Plan)
- Implement **User Authentication** (Django auth / JWT)
- Link tasks to users (ownership: each user manages their own tasks only)
- Add permission checks (no user can access another user’s tasks)
- Create endpoints to mark tasks **complete/incomplete** with timestamp
- Add task filters & sorting (status, priority, due date)

---

## Tech Stack
- Python 3
- Django 5
- Django REST Framework

---

## How to Run (so far)
1. Clone this repository:
   ```bash
   git clone https://github.com/esther-n-m/taskmanager-backend.git

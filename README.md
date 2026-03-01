# Django Job Portal

## 📌 Overview

Django Job Portal is a web application built using Django that displays job listings based on city.  
Users can click on a city (Hyderabad, Bangalore, Pune) and view all available jobs for that location.

This project demonstrates basic Django concepts including models, views, templates, URL routing, and database filtering.

---

## 🚀 Concepts Used

- Django Function-Based Views (FBV)
- Django Models
- Model Field Choices
- QuerySet Filtering (`filter()`)
- Dynamic URLs with parameters
- Django Template Language (DTL)
- Static Files (CSS)
- Admin Panel Customization
- SQLite Database

---

## 🏗 Project Structure
```
django-job-portal/
│
├── jobsproject/                 # Main Django Project Folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/             # (Ignored in git)
│
├── testapp/                     # Django App Folder
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── urls.py                  # (If created)
│
├── templates/
│   └── testapp/
│       ├── index.html
│       └── jobs.html
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── populate.py                  # (Your custom script)
├── requirements.txt
├── .gitignore
└── db.sqlite3                   # (Should NOT upload)
```

---

## ▶️ How to Run
- Install required packages `requirements.txt`
- Apply migrations
  ```
  python manage.py makemigrations
  python manage.py migrate

  ```
- Populate fake data `python populate.py`
- Run the server `python manage.py runserver`
- Open in browser send request `http://127.0.0.1:8000`

---

## Author & Contact
<strong>Rajat Kumar Bal</strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a>
<div align='center'>
  Made with 💖 by <strong> Rajat </strong>
</div>


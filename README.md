# Student Details

A simple student management project built with **Django**. It demonstrates Django models, templates, static files, media uploads, URL routing, and the built-in admin panel.

## Features

- Student details management
- Student profile image upload
- Student list and detail pages
- Django built-in admin panel
- Static CSS and images
- SQLite database

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

## Setup

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd student_project
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

#### Linux / MacOS:

```bash
source .venv/bin/activate
```

#### Windows (Command Prompt):

```bash
.venv\Scripts\activate
```

#### Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install django pillow
```

Apply migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main Pages

| URL               | Description        |
| ----------------- | ------------------ |
| `/`               | Home page          |
| `/students/`      | Student list       |
| `/students/<id>/` | Student details    |
| `/admin/`         | Django admin panel |

## Project Structure

```text
student_project/
├── students/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
├── student_project/
├── manage.py
└── db.sqlite3
```

> This project is created for learning and demonstrates basic Django concepts.

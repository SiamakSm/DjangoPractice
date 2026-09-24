
# Django Learning Project

A minimal Django project built as a hands-on learning exercise for technical interview preparation.

## Stack

- Python 3.14 / Django 6.1 / SQLite

## Setup

```bash
python3 -m venv venv && source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

## Key URLs

| URL                   | Description           |
| --------------------- | --------------------- |
| `/hello/`           | Simple HttpResponse   |
| `/greet/<name>/`    | Path parameter        |
| `/search/?q=...`    | Query parameter       |
| `/students/`        | List students from DB |
| `/students/create/` | POST form             |
| `/student-cbv/`     | Class-Based View      |
| `/admin/`           | Django Admin          |

## Concepts Covered

- Project vs App architecture
- Request lifecycle: `urls.py` → `views.py` → response
- Path & Query parameters
- HTML Templates & `render()`
- ORM: models, migrations, CRUD
- ForeignKey relationships
- N+1 Problem: diagnosed with `connection.queries`, fixed with `prefetch_related()`
- POST Forms & `{% csrf_token %}`
- Function-Based Views vs Class-Based Views
- Django Admin

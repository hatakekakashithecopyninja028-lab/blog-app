# The Margin — Django Blog

A full-featured Django blog with a clean editorial design.

## Features
- Posts with categories, tags, cover images
- Comment system
- Full-text search
- Pagination
- Django Admin for content management
- Responsive design

## Quick Start

```bash
# Install dependencies
pip install django pillow

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Then visit: http://127.0.0.1:8000

## Admin Panel
URL: http://127.0.0.1:8000/admin/
Credentials: admin / admin123

## Project Structure
```
blogsite/
├── blog/           # Blog app (models, views, urls, admin)
├── blogsite/       # Project settings & urls
├── templates/      # HTML templates
│   └── blog/
├── static/
│   └── css/style.css
└── manage.py
```

## Creating Content
1. Go to /admin/
2. Create Categories and Tags first
3. Create Posts — set status to "Published" to make them visible

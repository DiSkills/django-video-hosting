#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py createadmin

exec gunicorn django_video_hosting.wsgi:application -b 0.0.0.0:8000 --reload

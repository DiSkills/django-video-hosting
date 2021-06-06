# Anti-YouTube: Django 3.

Installing:

    python3 -m venv DirectoryVENV
    source DirectoryVENV/bin/activate
    pip install -r requirements.txt
    create directory "media" and create file "config.env"
    Include in "config.env":
        SECRET_KEY=<secret-key>
        DEFAULT_FROM_EMAIL=<default-email-address>
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

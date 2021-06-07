# Anti-YouTube: Django 3.

Installing:

    docker and docker-compose
    create directory "staticfiles"
    create directory "media"

    create file "config.env" with:
        SECRET_KEY=<secret-key>
        DEFAULT_FROM_EMAIL=anti_youtube@localhost
        DB_NAME=anti_youtube_db
        DB_USER=anti_youtube
        DB_PASSWORD=anti_youtube
        DB_HOST=posgresdb
        EMAIL_USER=<email-for-service>
        EMAIL_PASSWORD=<password-for-service>
        ADMIN_1=<your-email-admin>
        USERNAME_ADMIN=<username-for-createsuperuser>
        ADMIN_PASSWORD=<password-for-createsuperuser>

    docker-compose build
    docker-compose up

    if port 5432 listen:
        sudo service postgresql stop

    if need delete images for docker:
        docker system prune -a

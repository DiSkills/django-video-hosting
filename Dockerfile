FROM python:3.8

#Your work directory
WORKDIR /home/counter/programming_projects/django_video_hosting

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/home/counter/programming_projects/django_video_hosting/entrypoint.sh"]

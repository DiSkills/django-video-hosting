from django.core.mail import mail_managers
from django.template.loader import render_to_string

from django_video_hosting.settings import ALLOWED_HOSTS


def send_manager_about_new_video(video):
    """ New video """

    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'video': video, 'host': host}
    subject = render_to_string('email/subject.txt')
    body = render_to_string('email/body.txt', context)
    mail_managers(subject, body)

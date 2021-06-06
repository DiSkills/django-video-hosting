from django.template.loader import render_to_string

from django_video_hosting.settings import ALLOWED_HOSTS


def send_mail_about_activation(user):
    """ Send mail for activation user """

    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'host': host, 'user': user}
    subject = render_to_string('email/activation_subject.txt')
    body = render_to_string('email/activation_body.txt', context)
    user.email_user(subject, body)

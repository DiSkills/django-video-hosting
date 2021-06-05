from django.template.loader import render_to_string

from django_video_hosting.settings import ALLOWED_HOSTS


def send_mail_for_user_about_new_comment(comment, video, author=None):
    """ Send mail for user about new comment """

    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    if author:
        context = {'author': author, 'host': host, 'comment': comment, 'video': video}
    else:
        context = {'author': video.author, 'host': host, 'comment': comment, 'video': video}
        author = video.author
    subject = render_to_string('email/new_comment_subject.txt')
    body = render_to_string('email/new_comment_body.txt', context)
    if author.send_messages:
        author.email_user(subject, body)

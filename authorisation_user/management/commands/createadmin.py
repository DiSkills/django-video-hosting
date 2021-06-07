from django.core.management.base import BaseCommand

import os

from authorisation_user.models import AdvUser


class Command(BaseCommand):
    """ Create admin for docker """

    help = 'Create superuser for docker'

    def handle(self, *args, **options):
        username = os.environ.get('USERNAME_ADMIN')
        password = os.environ.get('ADMIN_PASSWORD')
        email = os.environ.get('ADMIN_1')

        superuser = AdvUser.objects.create_superuser(username, email, password)
        superuser.activated = True
        superuser.save()

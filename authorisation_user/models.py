from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    """ User """
    activated = models.BooleanField(default=False, verbose_name='User activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Send notification about new comments?')

    class Meta(AbstractUser.Meta):
        pass

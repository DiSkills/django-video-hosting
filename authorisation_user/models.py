from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from main.utilities import get_timestamp_path


class AdvUser(AbstractUser):
    """ User """

    activated = models.BooleanField(default=False, verbose_name='User activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Send notification about new comments?')
    subscription = models.ManyToManyField('AdvUser', verbose_name='Subscriptions', blank=True,
                                          related_name='subscriptions')
    subscriber = models.ManyToManyField('AdvUser', verbose_name='Subscribers', blank=True,
                                        related_name='subscribers')
    avatar = models.ImageField(verbose_name='Avatar', upload_to=get_timestamp_path)
    about = models.CharField(max_length=255, verbose_name='About me', blank=True, null=True)
    history = models.ManyToManyField('main.Video', verbose_name='History', blank=True)

    def follow(self, user):
        """ Follow """

        if not self.is_following(user):
            self.subscriptions.add(user)
            user.subscribers.add(self)

    def unfollow(self, user):
        """ Unfollow """

        if self.is_following(user):
            self.subscriptions.remove(user)
            user.subscribers.remove(self)

    def is_following(self, user):
        """ Is following user """

        return self.subscriptions.filter(username=user.username).count() > 0

    def get_absolute_url(self):
        """ Get absolute url """

        return reverse('accounts:profile', kwargs={'username': self.username})

    class Meta(AbstractUser.Meta):
        pass

from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    """ User """

    activated = models.BooleanField(default=False, verbose_name='User activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Send notification about new comments?')
    subscription = models.ManyToManyField('AdvUser', verbose_name='Subscriptions', blank=True,
                                          related_name='subscriptions')
    subscriber = models.ManyToManyField('AdvUser', verbose_name='Subscribers', blank=True,
                                        related_name='subscribers')

    def follow(self, user):
        if not self.is_following(user):
            self.subscriptions.add(user)
            user.subscribers.add(self)

    def unfollow(self, user):
        if self.is_following(user):
            self.subscriptions.remove(user)
            user.subscribers.remove(self)

    def is_following(self, user):
        return self.subscriptions.filter(username=user.username).count() > 0

    class Meta(AbstractUser.Meta):
        pass

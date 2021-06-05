from django.db import models
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    """ Comment """

    user = models.ForeignKey('authorisation_user.AdvUser', verbose_name='Author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    parent = models.ForeignKey('self', verbose_name='Parent comment', blank=True, null=True,
                               related_name='comment_children', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Date created comment')
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'

    @property
    def get_parent(self):
        if not self.parent:
            return ''
        return self.parent

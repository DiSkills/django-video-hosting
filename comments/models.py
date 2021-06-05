from django.db import models


class Comment(models.Model):
    """ Comment """

    user = models.ForeignKey('authorisation_user.AdvUser', verbose_name='Author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    parent = models.ForeignKey('self', verbose_name='Parent comment', blank=True, null=True,
                               related_name='comment_children', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Date created comment')
    is_child = models.BooleanField(default=False)
    video = models.ForeignKey('main.Video', on_delete=models.CASCADE, verbose_name='Video', related_name='comments')

    def __str__(self):
        return f'{self.user.username} - {self.video} - {self.text}'

    @property
    def get_parent(self):
        """ Get parent """

        if not self.parent:
            return ''
        return self.parent

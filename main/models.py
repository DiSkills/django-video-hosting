from django.db import models
from django.urls import reverse

from .utilities import get_timestamp_path


class Category(models.Model):
    """ Category """

    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Video(models.Model):
    """ Video """

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category', related_name='videos')
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Description')
    author = models.ForeignKey('authorisation_user.AdvUser', on_delete=models.CASCADE, verbose_name='Author',
                               related_name='videos')
    file = models.FileField(verbose_name='Video', upload_to=get_timestamp_path)
    blocked = models.BooleanField(default=False, verbose_name='Blocked video')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    preview = models.ImageField(verbose_name='Preview', null=True, blank=True, upload_to=get_timestamp_path)
    views = models.BigIntegerField(verbose_name='Views', default=0)
    subscriptions_views = models.BigIntegerField(verbose_name='With subscription views', default=0)
    private = models.BooleanField(default=False, verbose_name='Private video?')
    comments_on = models.BooleanField(default=True, verbose_name='Comments on?')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Get absolute url """

        return reverse('main:video_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['-created_at']


class LikeOrDislike(models.Model):
    """ Like """

    LIKE = 'like'
    DISLIKE = 'dislike'
    VOTE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike')
    )

    vote = models.CharField(max_length=10, verbose_name='Vote', choices=VOTE_CHOICES)
    video = models.ForeignKey(Video, verbose_name='Video', on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey('authorisation_user.AdvUser', verbose_name='User', on_delete=models.CASCADE,
                             related_name='vote')

    def __str__(self):
        return f'{self.user.username} - {self.vote}'

    class Meta:
        verbose_name = 'Like or Dislike'
        verbose_name_plural = 'Likes or Dislikes'

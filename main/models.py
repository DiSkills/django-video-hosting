from django.db import models
from django.urls import reverse

from .utilities import get_timestamp_path


class Category(models.Model):
    """ Category """

    name = models.CharField(max_length=255, verbose_name='Name category')
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Get absolute url """

        return reverse('main:video_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['-created_at']

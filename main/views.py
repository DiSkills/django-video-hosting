from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Video


class BaseView(ListView):
    """ Home """

    model = Video
    template_name = 'base.html'


class VideoDetailView(DetailView):
    """ Detail video """

    model = Video
    queryset = Video.objects.all()
    context_object_name = 'video'
    template_name = 'video_detail.html'
    slug_url_kwarg = 'slug'

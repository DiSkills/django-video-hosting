from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

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


class VideoStreamingResponse(View):
    """ Video player (chunked video upload) """

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(slug=kwargs['slug'])
        response = FileResponse(open(video.file.path, 'rb'))
        return response

from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from .models import Category, Video


class BaseView(View):
    """ Home """

    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        context = {'videos': videos}
        return render(request, 'base.html', context)

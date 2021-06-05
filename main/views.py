from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView

from .models import Video, Category, LikeOrDislike
from .forms import AddVideoForm, EditVideoForm
from .send_mail import send_manager_about_new_video


class BaseView(ListView):
    """ Home """

    model = Video
    template_name = 'base.html'


class CategoryDetailView(DetailView):
    """ Category Detail """

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'main/category_detail.html'
    slug_url_kwarg = 'slug'


class VideoDetailView(DetailView):
    """ Detail video """

    model = Video
    queryset = Video.objects.all()
    context_object_name = 'video'
    template_name = 'main/video_detail.html'
    slug_url_kwarg = 'slug'


class VideoStreamingResponse(View):
    """ Video player (chunked video upload) """

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(slug=kwargs['slug'])
        video.views += 1
        video.save()
        if request.user.is_authenticated:
            request.user.history.add(video)
            request.user.save()
        response = FileResponse(open(video.file.path, 'rb'))
        return response


class AddVideoView(LoginRequiredMixin, View):
    """ Add video """

    def get(self, request, *args, **kwargs):
        form = AddVideoForm(request.POST or None)
        context = {'form': form}
        return render(request, 'main/add_video.html', context)

    def post(self, request, *args, **kwargs):
        form = AddVideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.category = form.cleaned_data['category']
            new_video.title = form.cleaned_data['title']
            new_video.slug = form.cleaned_data['slug']
            new_video.description = form.cleaned_data['description']
            new_video.preview = form.cleaned_data['preview']
            new_video.file = form.cleaned_data['file']
            new_video.author = request.user
            new_video.save()
            send_manager_about_new_video(new_video)
            return redirect('main:video_detail', slug=new_video.slug)
        context = {'form': form}
        return render(request, 'main/add_video.html', context)


class EditVideoView(LoginRequiredMixin, UpdateView):
    """ Edit video """

    model = Video
    template_name = 'main/edit_video.html'
    form_class = EditVideoForm
    slug_url_kwarg = 'slug'


class LikeOrDislikeView(LoginRequiredMixin, View):
    """ Likes and Dislikes """

    def post(self, request, *args, **kwargs):
        slug = kwargs['slug']
        video = Video.objects.get(slug=slug)
        act = request.POST.get('act')
        user = request.user
        vote, created = LikeOrDislike.objects.get_or_create(user=user, video=video)
        vote.vote = act
        vote.save()
        return redirect('main:video_detail', slug=slug)

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import FileResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView

from .models import Video, Category, LikeOrDislike
from .forms import AddVideoForm, EditVideoForm
from .send_mail import send_manager_about_new_video
from .utilities import ranged
from comments.utils import create_comments_tree
from comments.forms import CommentForm


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

    def get_context_data(self, **kwargs):
        comments = kwargs['object'].comments.all()
        result = create_comments_tree(comments)
        comment_form = CommentForm()
        context = super().get_context_data(**kwargs)
        context['comments'] = result
        context['comment_form'] = comment_form
        return context

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(slug=kwargs['slug'])
        if video.private and video.author != request.user:
            raise HttpResponseForbidden('The author has hidden this video or it has been deleted!')
        elif video.blocked:
            raise HttpResponseForbidden('This video was blocked by moderation!')
        return super().get(request, *args, **kwargs)


class VideoStreamingResponse(View):
    """ Video player (chunked video upload) """

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(slug=kwargs['slug'])
        video.views += 1
        if request.user.is_authenticated:
            video.subscriptions_views += 1
            request.user.history.add(video)
            request.user.save()
        video.save()
        file = open(video.file.path, 'rb')
        file_size = video.file.size
        content_length = file_size
        content_range = request.headers.get('range')
        headers = {}
        # Search start and end position
        if content_range is not None:
            content_range = content_range.strip().lower()
            content_ranges = content_range.split('=')[-1]
            range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))
            range_start = max(0, int(range_start)) if range_start else 0
            range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
            content_length = (range_end - range_start) + 1
            file = ranged(file, start=range_start, end=range_end + 1)
            headers = {'Content-Range': f'bytes {range_start}-{range_end}/{file_size}'}
        response = FileResponse(file)
        response.set_headers({
            'Accept-Ranges': 'bytes',
            'Content-Length': str(content_length),
            **headers,
        })
        return response


class AddVideoView(LoginRequiredMixin, View):
    """ Add video """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.activated:
            raise HttpResponseForbidden('Your account is not activated!')
        return super().dispatch(request, *args, **kwargs)

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
            new_video.private = form.cleaned_data['private']
            new_video.comments_on = form.cleaned_data['comments_on']
            new_video.author = request.user
            new_video.save()
            send_manager_about_new_video(new_video)
            messages.add_message(request, messages.SUCCESS, 'You are new video has been added!')
            return redirect('main:video_detail', slug=new_video.slug)
        context = {'form': form}
        return render(request, 'main/add_video.html', context)


class EditVideoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Edit video """

    model = Video
    template_name = 'main/edit_video.html'
    form_class = EditVideoForm
    slug_url_kwarg = 'slug'
    success_message = 'You are video has been edited!'


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


class VideoForSearchView(View):
    """ Video for search """

    def get(self, request, *args, **kwargs):
        query = request.GET.get('search')
        if not query:
            videos = Video.objects.all()
        else:
            videos = Video.objects.filter(Q(title__icontains=query)) or \
                     Video.objects.filter(Q(author__username__icontains=query))
        context = {'video_list': videos}
        return render(request, 'base.html', context)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db import transaction
from django.views import View

from .forms import CommentForm
from .models import Comment
from main.models import Video


class CreateCommentView(LoginRequiredMixin, View):
    """ Create comment """

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST or None)
        video = Video.objects.get(slug=kwargs['slug'])
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.text = comment_form.cleaned_data['text']
            new_comment.video = video
            new_comment.parent = None
            new_comment.is_child = False
            new_comment.save()
        return redirect('main:video_detail', kwargs['slug'])


class CreateChildComment(LoginRequiredMixin, View):
    """ Create child comment """

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        video_slug = request.POST.get('slug')
        video = Video.objects.get(slug=video_slug)
        current_id = request.POST.get('id')
        text = request.POST.get('text')
        user = request.user
        parent = Comment.objects.get(id=int(current_id))
        is_child = False if not parent else True
        Comment.objects.create(user=user, text=text, video=video, parent=parent, is_child=is_child)
        return redirect('main:video_detail', video_slug)

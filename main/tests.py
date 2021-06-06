from django.test import TestCase, RequestFactory

from .views import *
from .models import Category, Video, LikeOrDislike
from .templatetags.video import get_vote_user, filter_video_count, filter_private_videos, likes_or_dislikes_count
from authorisation_user.models import AdvUser


class MainTestCase(TestCase):
    """ Main tests """

    def setUp(self) -> None:
        self.user = AdvUser.objects.create(username='test', password='test_password', activated=True)
        self.category = Category.objects.create(name='Games', slug='games')
        self.video = Video.objects.create(title='GTA VI', slug='gta-vi', description='GTA VI exists!',
                                          category=self.category, author=self.user)

    def tearDown(self) -> None:
        self.user.delete()
        self.category.delete()
        self.video.delete()

    def test_like(self):
        like = LikeOrDislike.objects.create(user=self.user, video=self.video, vote='like')
        self.assertEqual(self.video.votes.count(), 1)
        self.assertEqual(self.video.votes.first(), like)
        self.assertEqual(self.user.vote.first(), like)
        self.assertEqual(self.user.vote.count(), 1)

    def test_dislike(self):
        dislike = LikeOrDislike.objects.create(user=self.user, video=self.video, vote='dislike')
        self.assertEqual(self.user.vote.first(), dislike)
        self.assertEqual(self.video.votes.first(), dislike)
        video2 = Video.objects.create(title='GTA VI', slug='gta-vi-2', description='GTA VI exists!',
                                      category=self.category, author=self.user)
        LikeOrDislike.objects.create(user=self.user, video=video2, vote='dislike')
        self.assertEqual(self.user.vote.count(), 2)
        user2 = AdvUser.objects.create(username='test2', password='test_password')
        dislike3 = LikeOrDislike.objects.create(user=user2, video=self.video, vote='dislike')
        self.assertEqual(self.video.votes.count(), 2)
        self.assertEqual(self.video.votes.last().vote, dislike3.vote)

    def test_response_add_video(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = AddVideoView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_edit_video(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = EditVideoView.as_view()(request, slug=self.video.slug)
        self.assertEqual(response.status_code, 200)

    def test_base(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = BaseView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_video_view(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = VideoDetailView.as_view()(request, slug=self.video.slug)
        self.assertEqual(response.status_code, 200)

    def test_category_detail(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = CategoryDetailView.as_view()(request, slug=self.category.slug)
        self.assertEqual(response.status_code, 200)

    def test_get_vote_user(self):
        LikeOrDislike.objects.create(user=self.user, video=self.video, vote='like')
        vote = get_vote_user(self.video, self.user)
        self.assertEqual(vote, self.video.votes.first().vote)

    def test_filter_video_count(self):
        self.assertEqual(filter_video_count(Video.objects.all()), 1)
        self.video.private = True
        self.video.save()
        self.assertEqual(filter_video_count(Video.objects.all()), 0)

    def test_filter_private_videos(self):
        videos = filter_private_videos(Video.objects.all())
        self.assertEqual(videos.first(), self.video)
        self.video.private = True
        self.video.save()
        self.assertEqual(videos.count(), 0)

    def test_likes_or_dislikes_count(self):
        LikeOrDislike.objects.create(user=self.user, video=self.video, vote='like')
        count = likes_or_dislikes_count(self.video, 'like')
        self.assertEqual(count, 1)
        self.assertEqual(likes_or_dislikes_count(self.video, 'dislike'), 0)

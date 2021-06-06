from django.test import TestCase

from .models import Comment
from main.models import Category, Video
from authorisation_user.models import AdvUser


class CommentTestCase(TestCase):
    """ Comment tests """

    def setUp(self) -> None:
        self.user = AdvUser.objects.create(username='test', password='test')
        self.category = Category.objects.create(name='Games', slug='games')
        self.video = Video.objects.create(title='GTA VI', slug='gta-vi', description='GTA VI exists!',
                                          category=self.category, author=self.user)
        self.comment = Comment.objects.create(user=self.user, video=self.video, text='Good!')

    def tearDown(self) -> None:
        self.user.delete()
        self.category.delete()
        self.video.delete()
        self.comment.delete()

    def test_child_from_comment(self):
        comment_child = Comment.objects.create(user=self.user, video=self.video,
                                               text='Good!', is_child=True, parent=self.comment)
        self.assertEqual(self.comment.comment_children.first(), comment_child)
        self.assertEqual(self.comment.comment_children.count(), 1)
        self.assertEqual(comment_child.is_child, True)
        self.assertEqual(comment_child.parent, self.comment)
        self.assertEqual(comment_child.get_parent, self.comment)
        self.assertEqual(self.video.comments.count(), 2)
        self.assertEqual(self.video.comments.first(), self.comment)
        self.assertEqual(self.video.comments.last(), comment_child)

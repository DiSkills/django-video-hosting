from django.test import TestCase

from .models import AdvUser


class UserTestCase(TestCase):
    """ User tests """

    def setUp(self) -> None:
        self.user = AdvUser.objects.create(username='test', password='test')
        self.user2 = AdvUser.objects.create(username='test2', password='test2')

    def tearDown(self) -> None:
        self.user.delete()
        self.user2.delete()

    def test_follow_and_unfollow(self):
        self.user.follow(self.user2)
        self.assertEqual(self.user.is_following(self.user2), True)
        self.assertEqual(self.user.subscriptions.first(), self.user2)
        self.assertEqual(self.user2.subscribers.first(), self.user)
        self.assertEqual(self.user2.is_following(self.user), False)
        self.user.unfollow(self.user2)
        self.assertEqual(self.user.is_following(self.user2), False)
        self.assertEqual(self.user.subscriptions.count(), 0)
        self.assertEqual(self.user2.subscribers.count(), 0)

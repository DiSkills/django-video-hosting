from django import template

from ..models import LikeOrDislike

register = template.Library()


@register.simple_tag()
def likes_or_dislikes_count(video, vote):
    return LikeOrDislike.objects.filter(video=video, vote=vote).count()


@register.simple_tag()
def get_vote_user(video, user):
    return LikeOrDislike.objects.get(video=video, user=user).vote

from django import template

from ..models import LikeOrDislike, Video

register = template.Library()


@register.simple_tag()
def likes_or_dislikes_count(video, vote):
    """ Count likes or dislikes from video """

    return LikeOrDislike.objects.filter(video=video, vote=vote).count()


@register.simple_tag()
def get_vote_user(video, user):
    """ Get vote user """

    vote = LikeOrDislike.objects.filter(video=video, user=user)
    if vote:
        return vote.first().vote
    return ''


@register.simple_tag()
def filter_private_videos(videos):
    return videos.filter(private=False, blocked=False)


@register.filter
def filter_video_count(videos):
    return videos.filter(private=False, blocked=False).count()

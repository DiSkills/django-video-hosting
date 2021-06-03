from django import template

register = template.Library()


@register.simple_tag()
def follow_or_unfollow(user, account):
    """ Follow or Unfollow """
    return user.is_following(account)

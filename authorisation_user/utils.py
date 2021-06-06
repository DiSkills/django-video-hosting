from django.db.models import Sum


def get_count_all_views(user, statistic=False):
    """ Count all views for user """

    dictionary = user.videos.aggregate(Sum('views'), Sum('subscriptions_views'))
    if statistic:
        if dictionary['views__sum']:
            statistic_views = dictionary['subscriptions_views__sum'] / dictionary['views__sum'] * 100
            return statistic_views
        return 0
    return dictionary['views__sum'] or 0

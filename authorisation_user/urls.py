from django.urls import path

from .views import (
    RegistrationView,
    LoginUserView,
    LogoutUserView,
    ProfileView,
    FollowAndUnfollowView,
    SubscriptionsView,
    ChangeProfileView,
)

app_name = 'accounts'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/change/', ChangeProfileView.as_view(), name='profile_change'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:act>/<str:username>', FollowAndUnfollowView.as_view(), name='act_profile'),
    path('subscriptions/', SubscriptionsView.as_view(), name='subscriptions'),
]

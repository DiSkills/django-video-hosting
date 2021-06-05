from django.urls import path

from .views import (
    RegistrationView,
    LoginUserView,
    LogoutUserView,
    ProfileView,
    FollowAndUnfollowView,
    SubscriptionsView,
    ChangeProfileView,
    ChangePasswordView,
    RedirectProfileView,
    UserPopupView,
    HistoryView,
    DeleteVideoFromHistoryView,
    ResetPasswordView,
    ResetPasswordConfirmView,
)

app_name = 'accounts'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', RedirectProfileView.as_view(), name='profile_redirect'),
    path('profile/reset/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/reset/', ResetPasswordView.as_view(), name='reset_password'),
    path('profile/change/password/', ChangePasswordView.as_view(), name='password_change'),
    path('profile/change/', ChangeProfileView.as_view(), name='profile_change'),
    path('profile/<str:username>/popup/', UserPopupView.as_view(), name='user_popup'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:act>/<str:username>/', FollowAndUnfollowView.as_view(), name='act_profile'),
    path('subscriptions/', SubscriptionsView.as_view(), name='subscriptions'),
    path('history/delete/<str:slug>/', DeleteVideoFromHistoryView.as_view(), name='delete_from_history'),
    path('history/', HistoryView.as_view(), name='history'),
]

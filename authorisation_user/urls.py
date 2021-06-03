from django.urls import path

from .views import (
    RegistrationView,
    LogoutUserView
)

app_name = 'accounts'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]

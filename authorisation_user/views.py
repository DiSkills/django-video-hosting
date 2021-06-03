from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, Http404
from django.views import View

from .forms import RegistrationForm
from .models import AdvUser


class RegistrationView(View):
    """ Registration """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:base')
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'accounts/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.send_messages = form.cleaned_data['send_messages']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('accounts:profile')
        context = {'form': form}
        return render(request, 'accounts/registration.html', context)


class LoginUserView(LoginView):
    """ Login """

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class LogoutUserView(LoginRequiredMixin, View):
    """ Logout """

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main:base')


class ProfileView(View):
    """ Profile user """

    def get(self, request, *args, **kwargs):
        user = AdvUser.objects.filter(username=kwargs['username']).first()
        if not user:
            return Http404('Page not found')
        context = {'account': user}
        return render(request, 'accounts/profile.html', context)


class FollowAndUnfollowView(LoginRequiredMixin, View):
    """ Follow and Unfollow """

    def get(self, request, *args, **kwargs):
        user = AdvUser.objects.filter(username=kwargs['username']).first()
        if not user:
            return Http404('Page not found')
        act = kwargs.get('act')
        if act == 'follow':
            request.user.follow(user)
        elif act == 'unfollow':
            request.user.unfollow(user)
        return redirect('accounts:profile', username=user.username)

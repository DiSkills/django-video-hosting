from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegistrationForm


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


class LogoutUserView(LoginRequiredMixin, View):
    """ Logout """

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main:base')


class ProfileView(LoginRequiredMixin, View):
    """ Profile """

    def get(self, request, *args, **kwargs):
        return redirect('main:base')

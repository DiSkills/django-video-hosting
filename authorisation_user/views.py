from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.http import HttpResponseForbidden
from django.views import View

from .forms import RegistrationForm, ChangeProfileForm
from .models import AdvUser
from .send_mail import send_mail_about_activation
from .utils import get_count_all_views
from main.models import Video


class RedirectProfileView(View):
    """ Redirect after login """

    def get(self, request, *args, **kwargs):
        return redirect('accounts:profile', username=request.user.username)


class RegistrationView(View):
    """ Registration """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:base')
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'accounts/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.send_messages = form.cleaned_data['send_messages']
            new_user.avatar = form.cleaned_data['avatar']
            new_user.about = form.cleaned_data['about']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            login(request, user)
            send_mail_about_activation(new_user)
            messages.add_message(request, messages.SUCCESS,
                                 'Success registration! Please activate your account, mail send')
            return redirect('accounts:profile', username=user.username)
        context = {'form': form}
        return render(request, 'accounts/registration.html', context)


class LoginUserView(SuccessMessageMixin, LoginView):
    """ Login """

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_message = 'You are logged!'


class ChangeProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Profile change """

    model = AdvUser
    template_name = 'accounts/profile_change.html'
    form_class = ChangeProfileForm
    success_message = 'Your profile has been changed!'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangePasswordView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    """ Change Password User """

    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('main:base')
    success_message = 'Your password has been changed!'


class LogoutUserView(LoginRequiredMixin, View):
    """ Logout """

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You are has been logout!')
        return redirect('main:base')


class ProfileView(View):
    """ Profile user """

    def get(self, request, *args, **kwargs):
        user = AdvUser.objects.filter(username=kwargs['username']).first()
        if not user:
            return Http404('Page not found')
        views = get_count_all_views(user)
        context = {'account': user, 'views': views}
        if request.user == user:
            context['statistic'] = get_count_all_views(user, True)
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
            messages.add_message(request, messages.SUCCESS, 'You are has been follow!')
        elif act == 'unfollow':
            request.user.unfollow(user)
            messages.add_message(request, messages.SUCCESS, 'You are has been unfollow!')
        return redirect('accounts:profile', username=user.username)


class SubscriptionsView(LoginRequiredMixin, View):
    """ Subscriptions """

    def get(self, request, *args, **kwargs):
        subscriptions = request.user.subscriptions.all()
        context = {'subscriptions': subscriptions}
        return render(request, 'accounts/subscriptions.html', context)


class UserPopupView(View):
    """ User popup """

    def get(self, request, *args, **kwargs):
        user = AdvUser.objects.get(username=kwargs['username'])
        context = {'account': user}
        return render(request, 'accounts/user_popup.html', context)


class HistoryView(LoginRequiredMixin, View):
    """ History """

    def get(self, request, *args, **kwargs):
        return render(request, 'main/history.html')


class DeleteVideoFromHistoryView(LoginRequiredMixin, View):
    """ Delete video from history """

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(slug=kwargs['slug'])
        request.user.history.remove(video)
        request.user.save()
        messages.add_message(request, messages.WARNING, 'You are deleted video from history!')
        return redirect('accounts:history')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """ Reset password, email send """

    template_name = 'accounts/reset_password.html'
    subject_template_name = 'email/reset_subject.txt'
    email_template_name = 'email/reset_body.txt'
    success_url = reverse_lazy('main:base')
    success_message = 'Email sent!'


class ResetPasswordConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """ Reset password """

    template_name = 'accounts/reset_password_confirm.html'
    success_url = reverse_lazy('main:base')
    success_message = 'Your password has been reset!'


class ActivationView(LoginRequiredMixin, View):
    """ Activation profile """

    def get(self, request, *args, **kwargs):
        user = AdvUser.objects.get(username=kwargs['username'])
        if request.user != user:
            raise HttpResponseForbidden('You cannot activate someone else\'s account!')
        user.activated = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Your account has been activated!')
        return redirect('accounts:profile_redirect')

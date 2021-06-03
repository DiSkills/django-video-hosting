from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import AdvUser


class RegistrationForm(forms.ModelForm):
    """ Registration User """

    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    repeat_password = forms.CharField(label='Password (again)', widget=forms.PasswordInput, help_text='Password again')

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        if AdvUser.objects.filter(username=username).exists():
            raise ValidationError('Please use different username')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if AdvUser.objects.filter(email=email).exists():
            raise ValidationError('Please use a different email')
        return email

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        repeat_password = self.cleaned_data['repeat_password']
        if password and repeat_password and password != repeat_password:
            errors = {'repeat_password': ValidationError('The passwords entered do not match', code='password_mismatch')}
            raise ValidationError(errors)

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password', 'repeat_password', 'first_name', 'last_name',
                  'send_messages', 'avatar')


class ChangeProfileForm(forms.ModelForm):
    """ Profile change """

    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages', 'avatar')

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
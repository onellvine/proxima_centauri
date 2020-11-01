from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import NewUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'phone', 'password1', 'password2']
        widgets = {
            'user_name' : forms.TextInput(attrs = {'placeholder': 'Username'}),
            'phone'    : forms.TextInput(attrs = {'placeholder': 'Phone Format: +254712345678'}),
        }


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = NewUser
        fields = "__all__"

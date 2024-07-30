from django.contrib.auth.forms import UserCreationForm
from django import forms

from app.models import User


class UserForm(UserCreationForm):
    password1 = None
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password']

from django import forms
from django.contrib.auth.forms import UserCreationForm as USForm
from django.contrib.auth.models import User


class UserCreationForm(USForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
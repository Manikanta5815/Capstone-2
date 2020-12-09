from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class usersForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['User_Name','Email','Password']

from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationform(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)

    class meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name')

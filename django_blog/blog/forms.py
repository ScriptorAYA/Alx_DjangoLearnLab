from django import forms
from .models import Post, comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# -----------------------------------------------------------
# Custom Registration Form
# Extends Django's built-in UserCreationForm
# Adds required email field
# -----------------------------------------------------------

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# -----------------------------------------------------------
# Profile Update Form
# Allows user to update email and username
# -----------------------------------------------------------

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

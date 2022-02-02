from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User, Image, Post


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('product_name', 'product_description', 'product_price',
                  'product_category', 'location')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

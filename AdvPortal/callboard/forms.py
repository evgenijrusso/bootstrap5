from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Advert, AdvUser, AdditionalImage, Comment
# from .signals import post_register


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'

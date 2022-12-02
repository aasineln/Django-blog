from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    phone = forms.CharField(max_length=15, min_length=9, required=False, help_text='Телефон')

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'city', 'phone', 'password1', 'password2']

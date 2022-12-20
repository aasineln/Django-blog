from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from app_users.models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    phone_number = forms.CharField(max_length=15, min_length=9, required=False, help_text='Телефон')
    avatar = forms.ImageField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'city', 'phone_number', 'avatar', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phone_number']


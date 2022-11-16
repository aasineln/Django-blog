from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'text']

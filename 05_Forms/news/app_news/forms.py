from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=400)
    description = forms.CharField(max_length=500)
    tags = forms.CharField(max_length=400)

    class Meta:
        model = News
        fields = ['title', 'description', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']

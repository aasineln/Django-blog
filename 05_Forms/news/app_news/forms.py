from django import forms
from .models import News, Comment, NewsTags
from django.forms.models import inlineformset_factory

# NewsFormset = inlineformset_factory(News, NewsTags, extra=1)


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

from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=400)
    # description = forms.CharField(max_length=500)
    tags = forms.CharField(max_length=400)
    # photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = News
        fields = ['title', 'description', 'tags']


class ImageForm(forms.Form):
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        fields = ['photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
      

class MultiFilesForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UploadNewsForm(forms.Form):
    file = forms.FileField()

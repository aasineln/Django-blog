from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import News, Comment
from django.urls import reverse_lazy
from .forms import NewsForm, CommentForm


class NewsView(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()

class NewsDetailView(DetailView):
    template_name = 'app_news/news_detail.html'
    form_class = CommentForm
    model = News

    def get_context_data(self, **kwargs):
        news = super().get_object()
        context = super().get_context_data(**kwargs)
        context['comments_form'] = CommentForm()
        context['comments_list'] = Comment.objects.filter(news_id=news.id)
        return context

    def post(self, request, pk, **kwargs):
        comments_form = CommentForm(request.POST)
        if comments_form.is_valid():
            comments_form.cleaned_data['news_id'] = pk
            Comment.objects.create(**comments_form.cleaned_data)
            return HttpResponseRedirect(request.path_info)
        print('не зашёл')
        return render(request, 'app_news/news_detail.html', context={'comment_form': comments_form})


class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'description']


class NewsEditView(UpdateView):
    model = News
    fields = ['title', 'description']
    template_name_suffix = '_update_form'


class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('news')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['name', 'text']


class CommentEditView(UpdateView):
    model = Comment
    fields = ['name', 'text']
    template_name_suffix = '_update_form'


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('news')

# form_class = NewsForm
# template_name = 'app_news/news_edit.html'
#
# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['title'] = 'Добавление статьи'
#     context['description'] = description
#     return context

# class NewsEditView(View):
#     def get(self, request, news_id):
#         news = News.objects.get(id=news_id)
#         news_form = NewsForm(instance=news)
#         return render(request, 'app_news/news_edit.html', context={'news_form': news_form, 'news_id': news_id})
#
#     def post(self, request, news_id):
#         news = News.objects.get(id=news_id)
#         news_form = NewsForm(request.POST, instance=news)
#         if news_form.is_valid():
#             news.save()
#         return render(request, 'app_news/news_edit.html', context={'news_form': news_form, 'news_id': news_id})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import News
from .forms import NewsForm


class NewsView(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()


class NewsDetailView(DetailView):
    model = News


# class NewsCreateView(View):
#     def get(self, request):
#         news_form = NewsForm()
#         return render(request, 'app_news/news_create.html', context={'news_form': news_form})
#
#     def post(self, request):
#         news_form = NewsForm(request.POST)
#         if news_form.is_valid():
#             News.objects.create(**news_form.cleaned_data)
#             return HttpResponseRedirect('/news')
#         return render(request, 'app_news/news_create.html', context={'news_form': news_form})

class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'description']


class NewsEditView(UpdateView):
    model = News
    fields = ['title', 'description']
    template_name_suffix = '_update_form'

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

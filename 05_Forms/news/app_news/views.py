from _csv import reader

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import HiddenInput, CharField
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import News, Comment, ImageModel
from django.urls import reverse_lazy
from .forms import NewsForm, CommentForm, ImageForm, UploadNewsForm


class NewsView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'app_news/news_list.html'
    queryset = News.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['author'] = Author.objects.
        query = self.request.GET.get('news_sort', None)
        if query == 'first_new':
            news_list = News.objects.all().order_by('-created_at')
            context['news_list'] = news_list
            return context

        elif query == 'first_old':
            news_list = News.objects.all().order_by('created_at')
            context['news_list'] = news_list
            return context

        query = self.request.GET.get('q')
        if query:
            news_list = News.objects.filter(newstags__tag__icontains=query)
            context['news_list'] = news_list
            context['tag'] = query
            return context

        return context


class SearchResultsView(TemplateView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        self.user_query = query
        object_list = News.objects.filter(newstags__tag__icontains=query)
        return object_list


class TagNewsView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'app_news/news_list.html'
    queryset = News.objects.filter(is_active=True)


class NewsDetailView(DetailView):
    template_name = 'app_news/news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        news = super().get_object()
        context = super().get_context_data(**kwargs)
        context['comments_list'] = Comment.objects.filter(news_id=news.id)
        context['photo_list'] = ImageModel.objects.filter(news_id=news.id)
        comments_form = CommentForm()
        if self.request.user.is_authenticated:
            comments_form.fields['name'] = CharField(widget=HiddenInput(), required=False)
        context['comments_form'] = comments_form
        return context

    def post(self, request, pk, **kwargs):
        comments_form = CommentForm(request.POST)
        if self.request.user.is_authenticated:
            comments_form.fields['name'] = CharField(widget=HiddenInput(), required=False)
        if comments_form.is_valid():
            if request.user.is_authenticated:
                comments_form.cleaned_data['name'] = str(request.user)
            else:
                anon_user = comments_form.cleaned_data['name']
                comments_form.cleaned_data['name'] = ' '.join((anon_user, '(аноним)'))
            comments_form.cleaned_data['news_id'] = pk
            Comment.objects.create(**comments_form.cleaned_data)
            return HttpResponseRedirect(request.path_info)

        return render(request, 'app_news/news_detail.html', context={'comment_form': comments_form})


class NewsCreateView(UserPassesTestMixin, CreateView):
    model = News
    template_name = 'app_news/news_create.html'
    success_url = '/'
    form_class = NewsForm

    def test_func(self):
        return self.request.user.has_perm('app_news.add_news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_img'] = ImageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = NewsForm(request.POST)
        img_form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and img_form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            files = request.FILES.getlist('photo')
            for file in files:
                img = ImageModel(news=instance, photo=file)
                img.save()
        return redirect('/')


class NewsEditView(UpdateView):
    model = News
    fields = ['title', 'description']
    template_name_suffix = '_update_form'
    success_url = '/'


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/'


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


class NewsLoginView(LoginView):
    template_name = 'app_news/login.html'
    next_page = '/'


class NewsLogoutView(LogoutView):
    template_name = 'app_news/logout.html'
    next_page = '/'


class UploadNewsCsv(TemplateView):
    template_name = 'app_news/upload_news_csv.html'

    def get_context_data(self, **kwargs):
        context = super(UploadNewsCsv, self).get_context_data()
        context['form'] = UploadNewsForm()

        return context

    def post(self, request):
        upload_file_form = UploadNewsForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            query_info = {
                'updated_items': 0,
                'new_items': 0,
                'new_items_list': []
            }
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('cp1251').split('\r\n')
            csv_reader = reader(price_str, delimiter=";", quotechar='"')

            for row in csv_reader:
                if len(row) == 2:
                    try:
                        print(row)
                        News.objects.create(title=row[0], description=row[1])
                        query_info['new_items'] += 1
                        query_info['new_items_list'].append(row[0])
                    except BaseException as e:
                        print(e)

            return HttpResponse(content=f'Новости успешно загружены<br>{query_info}', status=200)

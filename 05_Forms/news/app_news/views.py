from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import HiddenInput, CharField
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView

from .models import News, Comment, NewsTags
from django.urls import reverse_lazy
from .forms import NewsForm, CommentForm


class NewsView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'app_news/news_list.html'
    queryset = News.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
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
    queryset = News.objects.filter(newstags__tag__icontains='java')
    # queryset = News.objects.filter(is_active=True)

    # def get(self):
    #     if self.request.user.has_perm('app_news.can_publish'):
    #         queryset = News.objects.all()


# def show_news(request, news_slug):
#     news = get_object_or_404(News, slug=news_slug)
#     return reverse('post', kwargs={'post_slug': self.slug})

# def news_list(request, tag_slug=None):
#     object_list = News.objects.all()
#     print(object_list)
#     tag = None
#
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         print(object_list)
#         object_list = object_list.filter(tags__in=[tag])
#
#     paginator = Paginator(object_list, 3)  # 3 поста на каждой странице
#     page = request.GET.get('page')
#     try:
#         news = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, поставим первую страницу
#         news = paginator.page(1)
#     except EmptyPage:
#         # Если страница больше максимальной, доставить последнюю страницу результатов
#         news = paginator.page(paginator.num_pages)
#     print(tag)
#     return render(request,
#                   'app_news/news_list.html',
#                   {'page': page,
#                    'news_list': news,
#                    'tag': tag})


class NewsDetailView(DetailView):
    template_name = 'app_news/news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        news = super().get_object()
        context = super().get_context_data(**kwargs)
        context['comments_list'] = Comment.objects.filter(news_id=news.id)
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


class NewsCreateView(UserPassesTestMixin, FormView):
    template_name = 'app_news/news_create.html'
    form_class = NewsForm
    success_url = '/'

    def test_func(self):
        return self.request.user.has_perm('app_news.add_news')

    def form_valid(self, form):
        form_title = form.cleaned_data['title']
        form_description = form.cleaned_data['description']
        form_tags = form.cleaned_data['tags']
        tag = NewsTags(tag=form_tags)
        tag.save()
        news = tag.news.create(title=form_title, description=form_description)
        news.save()
        return super().form_valid(form)


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

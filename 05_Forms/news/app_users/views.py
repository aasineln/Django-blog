from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View

from app_news.models import News
from .models import Profile
from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'app_users/register.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        city = form.cleaned_data.get('city')
        new_user = Profile.objects.create(user=user, city=city)
        group = Group.objects.get(name='Пользователи')
        new_user.user.groups.add(group)
        new_user.save()
        return redirect(self.success_url)


class ProfileView(View):
    def get(self, request):
        context = {}
        current_user_groups = request.user.groups.values_list("name", flat=True)
        context["users"] = Profile.objects.exclude(is_verified=True)
        context["news"] = News.objects.filter(is_active=False)
        context["is_users"] = "users" in current_user_groups
        return render(request, 'app_users/profile.html', context)

    # @permissions
    def post(self, request, **kwargs):
        to_verify_users_list = request.POST.getlist('users_list')
        to_publish_news = request.POST.getlist('news_list')

        for user_id in to_verify_users_list:
            user_id = int(user_id)
            user_profile = Profile.objects.get(id=user_id)
            user_profile.is_verified = True
            user_profile.save()

        for news_id in to_publish_news:
            news_id = int(news_id)
            news = News.objects.get(id=news_id)
            news.is_active = True
            news.save()

        return HttpResponseRedirect(request.path_info)

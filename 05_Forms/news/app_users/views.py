from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, UpdateView
from app_news.models import News
from .models import Profile, ProfileAvatar
from .forms import RegisterForm, UserForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'app_users/register.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
            avatar = form.cleaned_data['avatar']
            ProfileAvatar.objects.create(user=instance, avatar=avatar)

        return redirect('/')

    def form_valid(self, form):
        user = form.save()
        city = form.cleaned_data.get('city')
        phone_number = form.cleaned_data.get('phone_number')
        print(form.cleaned_data)
        new_user = Profile.objects.create(user=user, city=city, phone_number=phone_number)
        group = Group.objects.get(name='Пользователи')
        new_user.user.groups.add(group)
        new_user.save()
        return redirect(self.success_url)


class ProfileEditView(UpdateView):
    form_class = UserForm
    template_name = 'app_users/profile.html'
    model = User
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def test_func(self, request):
        return request.user.id == self.get_object()


class ProfileView(View):
    def get(self, request):
        context = {}
        current_user_groups = request.user.groups.values_list("name", flat=True)
        context["users"] = Profile.objects.exclude(is_verified=True)
        context["news"] = News.objects.filter(is_active=False)
        context["is_users"] = "users" in current_user_groups
        return render(request, 'app_users/profile.html', context)

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

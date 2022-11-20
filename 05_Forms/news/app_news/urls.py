from django.urls import path
from .views import NewsView, NewsDetailView, NewsCreateView, NewsEditView, NewsDeleteView, NewsLoginView, NewsLogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('create/', login_required(NewsCreateView.as_view()), name='create'),
    path('<int:pk>/edit/', login_required(NewsEditView.as_view()), name='edit'),
    path('<int:pk>/delete/', login_required(NewsDeleteView.as_view()), name='delete'),
    path('login/', NewsLoginView.as_view(), name='login'),
    path('logout/', NewsLogoutView.as_view(), name='logout')
]

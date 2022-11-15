from django.urls import path
from .views import NewsView, NewsDetailView, NewsCreateView, NewsEditView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('news/<int:news_id>/edit/', NewsEditView.as_view(), name='edit'),
]

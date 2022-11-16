from django.urls import path
from .views import NewsView, NewsDetailView, NewsCreateView, NewsEditView, NewsDeleteView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('news/<int:pk>/edit/', NewsEditView.as_view(), name='edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='delete'),
]

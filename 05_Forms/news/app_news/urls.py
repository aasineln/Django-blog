from django.urls import path
from .views import NewsView, NewsDetailView, NewsCreateView, NewsEditView, NewsDeleteView, NewsLoginView, \
    NewsLogoutView, SearchResultsView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('login/', NewsLoginView.as_view(), name='login'),
    path('logout/', NewsLogoutView.as_view(), name='logout'),
    # path('tag/<slug:slug>/', TagNewsView.as_view(), name='tag-news-list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
    path('create/', login_required(NewsCreateView.as_view()), name='create'),
    path('<int:pk>/edit/', login_required(NewsEditView.as_view()), name='edit'),
    path('<int:pk>/delete/', login_required(NewsDeleteView.as_view()), name='delete'),

]

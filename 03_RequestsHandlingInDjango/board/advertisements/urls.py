from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    path('advertisements/', views.Advertisements.as_view()),
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('categories/', views.categories_list, name='categories_list'),
    path('regions/', views.Regions.as_view()),
]

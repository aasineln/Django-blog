from django.urls import path
from . import views

urlpatterns = [
    path('advertisements', views.advertisements_list, name='advertisements_list'),
    path('item_1', views.item_1, name='item_1'),
    path('item_2', views.item_2, name='item_2'),
    path('item_3', views.item_3, name='item_3'),
    path('item_4', views.item_4, name='item_4'),
    path('item_5', views.item_5, name='item_5'),
]
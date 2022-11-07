from django.urls import path
from . import views
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('advertisements/', AdvertisementListView.as_view(), name='advertisement'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement-detail')
]

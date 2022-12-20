from django.urls import path
from .views import RegisterView, ProfileEditView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileEditView.as_view(), name='profile'),
    path('profile/edit', ProfileEditView.as_view(), name='profile'),
]

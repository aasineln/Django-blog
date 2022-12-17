from django.urls import path
from .views import some_view, update_prices, doc_form_upload, upload_files

urlpatterns = [
    path('items/', some_view, name='item-list'),
    path('update_prices/', update_prices, name='update_prices'),
    path('upload_doc_file/', doc_form_upload, name='upload_doc_file'),
    path('upload_files/', upload_files, name='upload_files'),
]

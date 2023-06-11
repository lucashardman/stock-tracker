from django.urls import path
from tracker.views import index, search

urlpatterns = [
    path('', index),
    path('search', search, name='search'),
]
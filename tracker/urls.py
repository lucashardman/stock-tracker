from django.urls import path
from tracker.views import index, search, persist

urlpatterns = [
    path('', index),
    path('search', search, name='search'),
    path('persist', persist, name='persist')
]
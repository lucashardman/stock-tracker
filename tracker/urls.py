from tracker.views import deletestock, index, search, persist
from django.urls import path

urlpatterns = [
    path('', index),
    path('search', search, name='search'),
    path('persist', persist, name='persist'),
    path('deletestock', deletestock, name='deletestock')
]
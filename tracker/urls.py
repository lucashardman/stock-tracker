from tracker.views import deletestock, index, search, persist, login_view, signup
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', index),
    path('search', search, name='search'),
    path('persist', persist, name='persist'),
    path('deletestock', deletestock, name='deletestock'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]
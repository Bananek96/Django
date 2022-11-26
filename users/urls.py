from django.urls import path
from . import views

from django.views.generic import ListView
from users.models import User

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('user_info', ListView.as_view(
        model=User,
        context_object_name='users',
        template_name='users/user_info.html'
    ), name='user_info'),
    path('rejestruj/', views.rejestruj, name='rejestruj'),
    path('loguj/', views.loguj_user, name='loguj'),
    path('wyloguj/', views.wyloguj_user, name='wyloguj'),
]

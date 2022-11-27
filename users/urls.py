from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('info/<int:pk>', views.EditUser.as_view(), name='user_info'),
    path('rejestruj/', views.signup, name='rejestruj'),
    path('loguj/', views.loguj_user, name='loguj'),
    path('wyloguj/', views.wyloguj_user, name='wyloguj'),
]

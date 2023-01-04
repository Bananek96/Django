from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('<int:pk>/', views.user_detail, name='index'),
    path("edit/<int:pk>/", views.edit_user_profile, name="user_info"),
    path('rejestruj/', views.SignUp.as_view(), name='rejestruj'),
    path('loguj/', views.loguj_user, name='loguj'),
    path('wyloguj/', views.wyloguj_user, name='wyloguj'),
]

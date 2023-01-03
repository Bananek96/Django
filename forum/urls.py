from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
	path('', views.posts_list, name='index'),
	path('post/<int:pk>', views.post_detail, name='post'),
	path('post/new', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<int:pk>/answer/', views.add_answer, name="add_answer")
]

from django.urls import path
from . import views
from . import posts

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('user/', views.user, name='user'),
    path('user/create/', views.userCreate, name='userCreate'),
    path('user/create/post', posts.userCreate, name='userCreate_post'),
]

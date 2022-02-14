from django.urls import path
from . import views
from . import posts

urlpatterns = [
    path('', views.index, name='index1'),
    path('index', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('user/login/', views.userLogin, name='userLogin'),
    path('user/login/post', posts.userLogin, name='userLogin_post'),
    path('user/', views.user, name='user'),
    path('user/create/', views.userCreate, name='userCreate'),
    path('user/create/post', posts.userCreate, name='userCreate_post'),
    path('user/file_upload', views.userUpload, name='userUpload' )
]

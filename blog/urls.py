from .views import  home,detail,post_create, register, user_login, user_logout,like_post,view_profile
from django.urls import path

urlpatterns = [
   path('',home , name='home'),
   path('register/',register, name='register'),
   path('login/',user_login, name='login'),
   path('logout/' , user_logout, name='logout'),
   path('post_create/' , post_create, name='post_create'),
   path('detail/<int:id>',detail, name='detail'),
   path('like/',like_post, name='like-post'),
   path('profile/',view_profile, name='profile'),
]

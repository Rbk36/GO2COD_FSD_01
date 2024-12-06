
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home
from .views import PostDetail, AddPost,EditPost, DeletePost, LikeView

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('post/<int:pk>',PostDetail.as_view(), name="post detail"),
    path('post/', AddPost.as_view(), name="Add Post"),
    path('editpost/<int:pk>', EditPost.as_view(), name="Edit Post"),
    path('post/<int:pk>/remove', DeletePost.as_view(), name="Delete Post"),
    path('post/<int:pk>/like', LikeView, name="like Post"),

]





from django.contrib import admin
from django.urls import path
from .views import Home
from .views import PostDetail

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('post/<int:pk>',PostDetail.as_view(), name="post detail")
]

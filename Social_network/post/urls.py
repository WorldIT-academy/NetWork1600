from django.urls import path
from .views import render_all_posts, render_create_posts


urlpatterns = [
    path("all/", render_all_posts,name='all_posts'),
    path('create/', render_create_posts)
]

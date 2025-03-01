from django.urls import path
from .views import *



urlpatterns = [
    path("all/", render_all_posts,name='all_posts'),
    path('create/', render_create_posts),
    path("create_tag/", render_create_tag),
    path("all_tags/", render_all_tags, name= "all_tags")
]

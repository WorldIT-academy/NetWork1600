from django.urls import path
from .views import render_all_posts


urlpatterns = [
    path("all/", render_all_posts)
]

from .views import *
from django.urls import path


urlpatterns = [
    path('registration/', render_registration)
]
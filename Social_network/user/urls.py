from .views import *
from django.urls import path


urlpatterns = [
    path('registration/', render_registration),
    path("login/", render_login, name="login"),
    path('welcome/', welcome, name="welcome"),
    path('logout/', logout_user, name = "logout"),
    path('all_profiles/', render_all_profiles, name='all_profiles' )
]
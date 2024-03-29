from abc import abstractstaticmethod
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.Login, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("profile", views.profile, name="profile")
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("add_user", add_user, name="add-user"),
    path("login_user", login_user, name="login-user"),
    path("dashboard", dashboard, name="dashboard")
]    
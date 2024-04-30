from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from .views import *


urlpatterns = [
   path("view-post", view_post, name="view_post"),
   path("get_weather", get_weather, name="get_weather"),
   path("list_post/", PostAPIView.as_view()),

]    
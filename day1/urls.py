
from django.contrib import admin
from django.urls import path
from .views import about,contact,home,login,register

urlpatterns = [
   
    path("about/",about),
    path("contact/",contact),
    path("home/",home),
    path("login/",login),
    path("register/",register)
]

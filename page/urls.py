from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name = "home"),
    path('login_page/', views.login_page),
    path("login_form/",views.login),
]

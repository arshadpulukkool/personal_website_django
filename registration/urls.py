from django.contrib import admin
from django.urls import path, include
from registration import views

urlpatterns = [
    path('register', views.register),


]
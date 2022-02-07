from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('personaldetails/', views.personald),
    path('home/', views.homepage),
    path('home/education/', views.education),
    path('home/resume', views.resume),
    path('home/aboutme/', views.aboutme),
    path('home/contact', views.contact),
    path('signup', views.signup),
    path('signin', views.signin),
    path('terms', views.terms),


]


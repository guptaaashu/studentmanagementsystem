from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.par_das, name='dash'),
]

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^accounts/login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    path('post/<int:pk>/', views.post_detail, name='student_detail'),
]

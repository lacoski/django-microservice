"""USER URL
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

from .views import HelloView, CheckView

urlpatterns = [
    path('', CheckView.as_view()),
    path('hello_view/', HelloView.as_view())
]

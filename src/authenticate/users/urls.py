"""USER URL
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

from .views import HelloView, MyTokenObtainPairView, CheckView

urlpatterns = [
    # path('api-token-auth/', views.obtain_auth_token),
    path('', CheckView.as_view()),
    path('hello_view/', HelloView.as_view()),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

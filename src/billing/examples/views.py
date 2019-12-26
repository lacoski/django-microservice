from django.conf import settings
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class CheckView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class HelloView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        test = request.user
        return Response(content)

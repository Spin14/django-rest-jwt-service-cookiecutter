from django.urls import path

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class HelloWorld(APIView):
    http_method_names = ['get']
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_200_OK,
            data={'detail': "Hello {{cookiecutter.email}}! Welcome to {{cookiecutter.app_name}}"},
            content_type='application/json')


urlpatterns = [
    path('', HelloWorld.as_view()),
]

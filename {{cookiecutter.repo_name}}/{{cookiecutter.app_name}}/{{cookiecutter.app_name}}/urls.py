from django.urls import path

from {{cookiecutter.app_name}}.views import status_view

urlpatterns = [
    path('', status_view),
]

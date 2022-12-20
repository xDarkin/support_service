from django.urls import path

from .api import convert

urlpatterns = [
    path("convert/", convert),
]

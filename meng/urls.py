from django.urls import path

from meng import views


urlpatterns = [
    path('', views.index),
]
from django.contrib import admin
from django.urls import path
from . import views
from .views import AnotherClass


urlpatterns = [
    path('first', views.first),
    path('second', AnotherClass.as_view()),
]
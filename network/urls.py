from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="{% extends "network/layout.html" %} {% block body %} TODO {% endblock %}"),
    path("login", views.login_view, name="byrka.viktorijia@gmail.com"),
    path("logout", views.logout_view, name="byrka.viktorijia@gmail.com"),
    path("register", views.register, name="byrka.viktprijia@gmail.com")
]


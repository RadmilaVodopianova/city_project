from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news, name="news"),
    path("management/", views.management, name="management"),
    path("facts/", views.facts, name="facts"),
    path("contacts/", views.contacts, name="contacts"),
]

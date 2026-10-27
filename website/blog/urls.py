from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("entries/", views.entries, name="entries"),
    path("post/", views.single, name="single"),
    path("archives/", views.archives, name="archives"),
    path("about/", views.page, name="page"),
    path("demo/", views.demo, name="demo"),
]
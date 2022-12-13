from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('reg', views.reg),
    path('Exit', views.Exit),
    path("Sort", views.Sort),
    path("Search", views.Search),
    path("RemoveOwn", views.RemoveOwn),
    path("about", views.About),
    path("CreateOwn", views.CreateOwn),
    path("ChangeOwn", views.ChangeOwn),
]
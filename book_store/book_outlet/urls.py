from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/<slug:slug>", views.book_detail, name="book_detail"),
    path("author/<slug:slug>", views.author_detail, name="author_detail"),
]

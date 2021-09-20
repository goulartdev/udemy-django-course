from django.urls import path

from . import views

urlpatterns = [
    path("", views.AllBooksView.as_view(), name="home"),
    path("book/<slug:slug>", views.BookDetailView.as_view(), name="book_detail"),
    path("author/<slug:slug>", views.AuthorBooksView.as_view(), name="author_detail"),
]

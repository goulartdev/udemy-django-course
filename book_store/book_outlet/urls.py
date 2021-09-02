from django.urls import path

from . import views

urlpatterns = [
    path("", views.books_list, name="books_list"),
    path("<slug:slug>", views.book_detail, name="book_detail"),
]

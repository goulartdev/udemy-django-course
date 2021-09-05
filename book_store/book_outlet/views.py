from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Author, Book


def home(request):
    books = Book.objects.all().order_by("rating")
    rating_avg = books.aggregate(Avg("rating")).get("rating__avg")

    template_data = {
        "books": books,
        "total_number_of_books": books.count(),
        "average_rating": rating_avg,
    }

    return render(request, "book_outlet/home.html", template_data)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    template_data = {
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "rating": book.rating,
        "is_bestseller": book.is_bestseller,
        "price": book.price,
    }

    return render(request, "book_outlet/book_detail.html", template_data)


def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    rating_avg = author.books.aggregate(Avg("rating")).get("rating__avg")

    template_data = {
        "name": author.name,
        "books": author.books.all(),
        "number_of_books": author.books.count(),
        "average_rating": rating_avg,
    }

    return render(request, "book_outlet/author_detail.html", template_data)

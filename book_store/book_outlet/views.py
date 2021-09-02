from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Book


def books_list(request):
    books = Book.objects.all().order_by("rating")
    rating_avg = books.aggregate(Avg("rating")).get("rating__avg")

    template_data = {
        "books": books,
        "total_number_of_books": books.count(),
        "average_rating": rating_avg,
    }

    return render(request, "book_outlet/books_list.html", template_data)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    template_data = {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestseller,
    }

    return render(request, "book_outlet/book_detail.html", template_data)

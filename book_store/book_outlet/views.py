from django.shortcuts import get_object_or_404, render
from django.db.models import Avg, Q
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.views.generic.list import MultipleObjectMixin

from .models import Author, Book

PAGINATE_BOOKS_BY = 15


class AllBooksView(ListView):
    template_name = "book_outlet/home.html"
    model = Book
    context_object_name = "books"
    paginate_by = PAGINATE_BOOKS_BY

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_queryset(queryset)

    def get_ordering(self):
        return self.request.GET.get("order_by", "author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_by"] = self.get_ordering()
        context["search_value"] = self.get_search_value()

        return context

    def filter_queryset(self, queryset):
        value = self.get_search_value()

        if value:
            queryset = queryset.filter(
                Q(title__contains=value) | Q(author__name__contains=value)
            )

        return queryset

    def get_search_value(self):
        return self.request.GET.get("search_value", "")


class BookDetailView(DetailView):
    template_name = "book_outlet/book_detail.html"
    model = Book
    context_object_name = "book"


class AuthorBooksView(DetailView, MultipleObjectMixin):
    template_name = "book_outlet/author_detail.html"
    model = Author
    context_object_name = "author"
    paginate_by = PAGINATE_BOOKS_BY

    def get_context_data(self, **kwargs):
        order_by = self.get_ordering()
        books = self.object.books.all().order_by(order_by)

        context = super().get_context_data(object_list=books.all(), **kwargs)

        context["books"] = context["object_list"]
        context["order_by"] = order_by
        context["number_of_books"] = books.count()
        context["average_rating"] = books.aggregate(Avg("rating")).get("rating__avg")

        return context

    def get_ordering(self):
        return self.request.GET.get("order_by", "author")


## Another way of doing AuthorBooksView

# class AuthorBooksView(AllBooksView):
#     template_name = "book_outlet/author_detail.html"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         author_slug = self.get_author_slug()

#         return queryset.filter(author__slug=author_slug)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         books = self.get_queryset()
#         author_slug = self.get_author_slug()

#         author = Author.objects.get(slug=author_slug)

#         context["author"] = author
#         context["number_of_books"] = books.count()
#         context["average_rating"] = books.aggregate(Avg("rating")).get("rating__avg")
#         context["order_by"] = self.get_ordering()

#         return context

#     def get_ordering(self):
#         return self.request.GET.get("order_by", "author")

#     def get_author_slug(self):
#         return self.kwargs["slug"]

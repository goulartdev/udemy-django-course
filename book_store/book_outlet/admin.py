from django.contrib import admin
from .models import Address, Book, Author, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "is_bestseller", "rating")
    list_display = ("title", "author", "is_bestseller", "rating")


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)

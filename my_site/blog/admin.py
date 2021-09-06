from django.contrib import admin
from .models import Blog, Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "get_tags")
    list_filter = ("author", "date", "tags")

    def get_tags(self, obj):
        return obj.get_tags()

    get_tags.short_description = "Tags"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")

    def full_name(self, obj):
        return obj.full_name()

    full_name.short_description = "Author"


class BlogAdmin(admin.ModelAdmin):
    list_display = ("header_text", "author")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)

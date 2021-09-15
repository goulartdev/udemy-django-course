from django.contrib import admin
from .models import Blog, Post, Author, Tag, PostComment


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


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "email", "date")
    list_filter = ("name", "post", "date")


class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("caption",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(PostComment, PostCommentAdmin)

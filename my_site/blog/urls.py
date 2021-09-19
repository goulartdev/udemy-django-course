from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="blog_home"),
    path("posts", views.AllPostsView.as_view(), name="all_posts"),
    path("posts/bookmark", views.BookmarkView.as_view(), name="bookmark"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
    path("tags/<slug:slug>", views.PostsByTagView.as_view(), name="tag_view"),
    path("my-bookmarks", views.MyBookmarksView.as_view(), name="my_bookmarks"),
]

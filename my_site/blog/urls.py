from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="blog_home"),
    path("posts", views.all_posts, name="all_posts"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail"),
]

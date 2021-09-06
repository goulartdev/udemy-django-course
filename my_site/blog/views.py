from django.shortcuts import render, get_object_or_404
from .models import Blog, Post

profile = {
    "name": "Djonathan",
    "shortname": "Dj",
    "welcome": "Hi, I am Djonathan and I love to blog about tech and the world!",
    "about": """
        I Love Programming, I love to help others and I enjoy exploring new
        technologies in generel.

        My goal is to keep on growing as a developer - and if I could help you
        do the same, I'd be very happy!
    """,
}

LATEST_POSTS_LIMIT = 3


def get_blog():
    return get_object_or_404(Blog)


def home(request):
    latest_posts = Post.objects.all()[:LATEST_POSTS_LIMIT]
    blog = get_blog()

    page_data = {
        "blog": blog,
        "posts": latest_posts,
    }

    return render(request, "blog/home.html", page_data)


def all_posts(request):
    posts = Post.objects.all()
    blog = get_blog()

    page_data = {
        "blog": blog,
        "posts": posts,
    }

    return render(request, "blog/all-posts.html", page_data)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tags = post.tags.all()
    blog = get_blog()

    page_data = {
        "blog": blog,
        "post": post,
        "tags": tags,
    }

    return render(request, "blog/post-detail.html", page_data)

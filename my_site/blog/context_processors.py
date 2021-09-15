from django.shortcuts import get_object_or_404
from .models import Blog


def add_blog_data(request):
    blog = get_object_or_404(Blog)

    return {
        "blog": blog,
    }

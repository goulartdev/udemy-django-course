from django.shortcuts import render
from datetime import datetime

# Create your views here.

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

fromisoformat = datetime.fromisoformat

posts = [
    {
        "slug": "hike-in-the-mountains",
        "title": "Mountain Hiking",
        "author": "Djonathan",
        "image": "mountains.jpg",
        "created_date": fromisoformat("2021-07-08T14:41:54-05:00"),
        "excerpt": """
            There's nothin like the views you get when hiking in the
            mountains! And I wasn't even prepared for what happened
            whilst I was enjoying the view!
        """,
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
    },
    {
        "slug": "programming-is-fun",
        "title": "Programming Is Great!",
        "author": "Djonathan",
        "image": "coding.jpg",
        "created_date": fromisoformat("2021-07-12T12:23:54-05:00"),
        "excerpt": """
            Did you ever spend hours searching that one error in your code? Yep -
            that's what happened to me yesterday...
        """,
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
    },
    {
        "slug": "into-the-woods",
        "title": "Nature At Its Best",
        "author": "Djonathan",
        "image": "woods.jpg",
        "created_date": fromisoformat("2021-07-20T10:54:12-05:00"),
        "excerpt": """
            Nature is amazing! The amount of inspiration I get when walking in nature
            is incredible!""",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
    },
]


LATEST_POSTS_LIMIT = 3


def get_sorted_posts():
    return sorted(posts, key=lambda post: post.get("created_date"))


def find_post(slug):
    return next(post for post in posts if post.get("slug") == slug)


def home(request):
    latest_posts = get_sorted_posts()[-LATEST_POSTS_LIMIT:]

    page_data = {
        "profile": profile,
        "posts": latest_posts,
    }

    return render(request, "blog/home.html", page_data)


def all_posts(request):
    page_data = {
        "profile": profile,
        "posts": get_sorted_posts(),
    }

    return render(request, "blog/all-posts.html", page_data)


def post_detail(request, slug):
    post = find_post(slug)

    page_data = {
        "profile": profile,
        "post": post,
    }

    return render(request, "blog/post-detail.html", page_data)

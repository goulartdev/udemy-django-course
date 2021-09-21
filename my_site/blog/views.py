from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import CreateView, ListView
from django.views import View

from .models import Post, PostComment
from .forms import AddCommentForm

LATEST_POSTS_LIMIT = 3


class Home(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:LATEST_POSTS_LIMIT]

        return data


class PostDetailView(View):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"
    comments_limit = 5

    def get(self, request, slug):
        context = self.get_context(request, slug, AddCommentForm())

        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = AddCommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        context = self.get_context(request, slug, comment_form)

        return render(request, "blog/post-detail.html", context)

    def get_context(self, request, slug, comment_form):
        post = get_object_or_404(Post, slug=slug)

        comments_limit = self.get_comments_limit()
        total_comments = post.comments.count()

        return {
            "post": post,
            "is_marked": post.id in request.session.get("bookmarks", []),
            "tags": post.tags.all(),
            "comments": post.comments.all()[:comments_limit],
            "form": comment_form,
            "comments_limit": comments_limit,
            "total_comments": total_comments,
        }

    def get_comments_limit(self):
        try:
            return int(self.request.GET.get("comments_limit", self.comments_limit))
        except ValueError:
            return self.comments_limit


class AddCommentView(CreateView):
    template_name = "blog/post-detail.html"
    model = PostComment
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse("post_detail", args=[self.object.post.slug])


class BookmarkView(View):
    def post(self, request):
        post_id = request.POST["post_id"]
        post = get_object_or_404(Post, pk=post_id)

        bookmarks = request.session.get("bookmarks", [])

        if post.id in bookmarks:
            bookmarks.remove(post.id)
        else:
            bookmarks.append(post.id)

        request.session["bookmarks"] = bookmarks

        return HttpResponseRedirect(reverse("post_detail", args=[post.slug]))


class AllPostsView(ListView):
    template_name = "blog/posts-list.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title()

        return context

    def get_page_title(self):
        return "All My Posts"


class PostsByTagView(AllPostsView):
    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.filter(tags__slug=self.kwargs["slug"])

    def get_page_title(self):
        tag = self.kwargs["slug"]
        return f"{tag} Posts"


class MyBookmarksView(AllPostsView):
    template_name = "blog/posts-list.html"

    def get_queryset(self):
        bookmarks = self.request.session.get("bookmarks")

        if bookmarks:
            return Post.objects.filter(id__in=bookmarks)

        return []

    def get_page_title(self):
        return "My Bookmarks"

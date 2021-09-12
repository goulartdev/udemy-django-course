from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = reverse_lazy("thank-you")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank You!!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_id = self.request.session.get("favorite_review_id")

        context["is_favorite"] = favorite_id == str(self.object.id)

        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        review = Review.objects.get(pk=review_id)

        request.session["favorite_review_id"] = review_id
        print(review)
        return HttpResponseRedirect(reverse("review-detail", args=[review_id]))

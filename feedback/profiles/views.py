from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import UserProfile


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfile
    context_object_name = "profiles"


# class CreateProfileView(CreateView):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submited = ProfileForm(request.POST, request.FILES)

#         if submited.is_valid():
#             image = request.FILES["user_image"]
#             profile = UserProfile(image=image)

#             profile.save()

#             return HttpResponseRedirect("/profiles")

#         return render(request, "profiles/create_profile.html", {"form": submited})

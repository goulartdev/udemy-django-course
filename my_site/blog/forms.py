from django import forms

from .models import PostComment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ("name", "email", "text")

        labels = {
            "text": "Comment",
        }

from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(
#         required=True,
#         min_length=5,
#         max_length=20,
#         error_messages={
#             "required": "Your username must not be empty",
#         },
#     )

#     review_text = forms.CharField(
#         label="Your feedback", widget=forms.Textarea, max_length=200
#     )

#     rating = forms.IntegerField(min_value=1, max_value=5, required=True)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ['username', 'review_text', 'rating']
        # exclude = ['some_field_to_exclude]

        labels = {
            "review_text": "Your feedback",
        }

        error_messages = {
            "username": {
                "required": "Your username must not be empty",
            },
        }

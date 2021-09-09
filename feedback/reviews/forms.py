from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=5,
        max_length=20,
        error_messages={
            "required": "Your username must not be empty",
        },
    )

    review_test = forms.CharField(
        label="Your feedback", widget=forms.Textarea, max_length=200
    )

    rating = forms.IntegerField(min_value=1, max_value=5, required=True)

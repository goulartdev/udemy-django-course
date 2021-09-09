from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)


class Review(models.Model):
    username = models.CharField(max_length=20, validators=[MinLengthValidator(5)])
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, default="", null=False, unique=True)
    rating = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestseller = models.BooleanField(default=False)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title} ({self.rating})"

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    address = models.OneToOneField(Address, on_delete=CASCADE, null=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(
        max_length=80, default="", null=False, unique=True, blank=True
    )
    rating = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author, on_delete=CASCADE, null=True, related_name="books"
    )
    is_bestseller = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, default="")
    price = models.FloatField(default=0)
    published_countries = models.ManyToManyField(Country)
    cover = models.ImageField(upload_to="covers")

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title} ({self.rating})"

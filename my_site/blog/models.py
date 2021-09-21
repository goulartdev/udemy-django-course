from django.db import models
from django.db.models.deletion import RESTRICT, CASCADE
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to="authors")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.caption)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    header_image = models.ImageField(upload_to="posts")
    excerpt = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=RESTRICT, related_name="posts")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[MinLengthValidator(200)])
    tags = models.ManyToManyField(Tag, related_name="posts")

    class Meta:
        ordering = ["-date"]
        get_latest_by = ["-date"]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    text = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        get_latest_by = ["-date"]


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=RESTRICT, related_name="blogs")
    header_text = models.CharField(max_length=15)
    welcome_mesage = models.CharField(max_length=150)
    about = models.TextField(max_length=500)

    def save(self, *args, **kwargs) -> None:
        if not self.pk and Blog.objects.exists():
            raise ValidationError("There can only be one Blog instance")

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.header_text

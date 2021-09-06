from django.db import models
from django.db.models.deletion import RESTRICT
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    # shortname = models.CharField(max_length=5)
    email = models.EmailField()
    # welcome_mesage = models.TextField(max_length=150)
    # about = models.TextField(max_length=300)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    excerpt = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=RESTRICT, related_name="posts")
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[MinLengthValidator(200)])
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["-date"]
        get_latest_by = ["-date"]

    def get_absolute_url(self):
        return reverse("auto_now_add", kwargs={"slug": self.slug})

    def get_tags(self):
        return ", ".join([tag.caption for tag in self.tags.all()])

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


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

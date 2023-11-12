import re
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


# phone validation for model: User
def validate_phone(value):
    if re.search(r"\d{1}\(\d{3}\)\d{3}-\d{2}-\d{2}", value) is None:
        raise ValidationError(
            "Phone number must contain only 11 digits in format _(___)___-__-__"
        )
    else:
        return f"+{value}"


class User(AbstractUser):
    phone = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_phone],
        verbose_name="Phone number",
        help_text="Phone number must contain only 11 digits in format _(___)___-__-__",
    )

    def __str__(self):
        return f"{self.username}, email: ({self.email})"


class Fact(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Title",
        help_text="Title of the fact",
    )
    description = models.TextField(
        max_length=1000,
        blank=False,
        null=False,
        verbose_name="Description",
        help_text="Description of the fact",
    )

    def __str__(self):
        return self.title


class NewsArticle(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="Title",
        help_text="Title of the News & Article",
    )

    author = models.CharField(
        max_length=255,
        default="Anonymous",
        verbose_name="Author",
        help_text="Author of the News & Article",
    )

    tags = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Tags",
        help_text="Tags for the News & Article",
    )

    publish_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="Publish date",
        help_text="Publish date of the News & Article",
        auto_now_add=False,
    )

    description = models.TextField(
        max_length=1000,
        blank=False,
        null=False,
        verbose_name="Description",
        help_text="Main content of the News & Article",
    )

    def __str__(self):
        return f"News|Article: {self.title}"

    class Meta:
        ordering = ["-publish_date"]
        verbose_name_plural = "News & Articles"


class Comment(models.Model):
    text = models.TextField(
        max_length=1000,
        blank=False,
        null=False,
        verbose_name="Comment",
        help_text="Comment",
    )

    publish_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="Publish date",
        help_text="Publish date of the comment",
        auto_now_add=False,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Comment - Author",
        help_text="Author of the comment",
        related_name="comment_author",
        null=False,
        blank=False,
    )

    article = models.ForeignKey(
        NewsArticle,
        on_delete=models.CASCADE,
        verbose_name="Comment - Article",
        help_text="Commented article",
        related_name="comment_article",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Comment: {self.text} by {self.author}. Publish date: {self.publish_date}. Article: {self.article}"


class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} saved {self.article.title}"

    class Meta:
        verbose_name_plural = "Saved Articles"

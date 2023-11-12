import re
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

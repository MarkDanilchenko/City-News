from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        required=True,
        label="Email",
        help_text="Enter a valid email address",
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        label="Phone number",
        help_text="Phone number must contain only 11 digits in format _(___)___-__-__",
    )

    class Meta:
        model = models.User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "phone",
        )


class FactForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        required=True,
        label="Title",
        help_text="Title of the fact",
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={}),
        max_length=1000,
        required=True,
        label="Description",
        help_text="Description of the fact",
    )

    class Meta:
        model = models.Fact
        fields = ("title", "description")

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "phone",
        "date_joined",
        "last_login",
    )
    list_filter = ("username",)
    search_fields = ("username",)


admin.site.register(models.User, CustomUserAdmin)


class FactAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Title of the fact", {"fields": ("title",)}),
        ("Description of the fact", {"fields": ("description",)}),
    )

    list_display = ("title", "description")
    list_filter = ("title",)
    search_fields = ("title",)


admin.site.register(models.Fact, FactAdmin)


class NewsArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Title", {"fields": ("title",)}),
        ("Author", {"fields": ("author",)}),
        ("Tags", {"fields": ("tags",)}),
        ("Publish date", {"fields": ("publish_date",)}),
        ("Description", {"fields": ("description",)}),
    )

    list_display = ("title", "author", "tags", "publish_date")
    list_filter = ("title", "publish_date")
    search_fields = ("title", "tags", "author")


admin.site.register(models.NewsArticle, NewsArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Comment text", {"fields": ("text",)}),
        ("Publish date", {"fields": ("publish_date",)}),
        ("Author and Article", {"fields": ("author", "article")}),
    )

    list_display = ("text", "publish_date", "author", "article")
    list_filter = ("publish_date", "author", "article")
    search_fields = ("text", "publish_date", "author", "article")


admin.site.register(models.Comment, CommentAdmin)


class SavedArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ("User", {"fields": ("user",)}),
        ("Article", {"fields": ("article",)}),
    )

    list_display = ("user", "article")
    list_filter = ("user", "article")
    search_fields = ("user", "article")


admin.site.register(models.SavedArticle, SavedArticleAdmin)

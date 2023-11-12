from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'phone', 'date_joined', 'last_login')
    list_filter = ('username',)
    search_fields = ('username',)


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

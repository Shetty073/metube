from string import ascii_lowercase, digits
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from shortuuid.django_fields import ShortUUIDField

from metube.identity_portal.managers import AppUserManager


class AppUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="id_",
        alphabet=f"{ascii_lowercase}{digits}"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AppUserManager()


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class AppUserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "is_staff", "is_superuser")

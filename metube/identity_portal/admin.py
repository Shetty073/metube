from django.contrib import admin
from metube.identity_portal.models import AppUser, AppUserAdmin

# Register your models here.
admin.site.register(AppUser, AppUserAdmin)

from django.db import models
from django.contrib import admin

from metube.identity_portal.models.app_user import AppUser
from metube.upload_portal.models.content import Content


class Rating(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='ratings')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()  # Example: 1 to 5

    def __str__(self):
        return f'Rating {self.rating} by {self.user.username} for {self.content.title}'

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'rating')
    search_fields = ('user__username', 'content__title')
    list_filter = ('rating',)

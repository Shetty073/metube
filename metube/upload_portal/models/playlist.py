from django.db import models
from django.contrib import admin

from metube.identity_portal.models.app_user import AppUser
from metube.upload_portal.models.content import Content


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='playlists')
    videos = models.ManyToManyField(Content, related_name='playlists')

    def __str__(self):
        return f'Playlist {self.name} by {self.user.username}'

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at',)
    filter_horizontal = ('videos',)

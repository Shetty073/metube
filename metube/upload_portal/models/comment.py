from django.db import models
from django.contrib import admin

from metube.identity_portal.models.app_user import AppUser
from metube.upload_portal.models.content import Content


class Comment(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='comments')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.content.title}'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'text', 'created_at')
    search_fields = ('user__username', 'content__title', 'text')
    list_filter = ('created_at',)
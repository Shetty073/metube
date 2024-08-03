from django.db import models
from django.contrib import admin


class Tag(models.Model):
    PERFORMER = 'star'
    CONTENT = 'content'
    TAG_TYPE_CHOICES = [
        (PERFORMER, 'Star'),
        (CONTENT, 'Content')
    ]

    name = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=10, choices=TAG_TYPE_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.tag_type})'

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tag_type')
    search_fields = ('name', 'tag_type')
    list_filter = ('tag_type',)
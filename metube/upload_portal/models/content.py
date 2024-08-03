import os
import re
from django.db import models
from django.contrib import admin
import cv2
from django.core.files import File

from metube.identity_portal.models.app_user import AppUser
from metube.upload_portal.models.category import Category
from metube.upload_portal.models.star import Star
from metube.upload_portal.models.tag import Tag


# Utility function for snake_case conversion
def to_snake_case(value):
    value = re.sub(r'[\W_]+', '_', value)
    return value.lower()

# Functions to generate file paths
def get_content_file_path(instance, filename):
    base, ext = os.path.splitext(filename)
    snake_case_title = to_snake_case(instance.title)
    return f'contents/{snake_case_title}{ext}'

def generate_thumbnail_from_video(file_path, thumbnail_path):
    cap = cv2.VideoCapture(file_path)
    
    if not cap.isOpened():
        raise ValueError("Error opening video file")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    mid_frame = total_frames // 2

    cap.set(cv2.CAP_PROP_POS_FRAMES, mid_frame)

    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite(thumbnail_path, frame)
    
    cap.release()

class Content(models.Model):
    VIDEO = 'video'
    MUSIC = 'music'
    CONTENT_TYPE_CHOICES = [
        (VIDEO, 'Video'),
        (MUSIC, 'Music')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=5, choices=CONTENT_TYPE_CHOICES)
    file = models.FileField(upload_to=get_content_file_path, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='contents', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='contents')
    tags = models.ManyToManyField(Tag, limit_choices_to={'tag_type': Tag.CONTENT}, related_name='contents')
    stars = models.ManyToManyField(Star, related_name='contents')
    uploaded_by = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, related_name='uploaded_contents')

    def __str__(self):
        return self.title

    def save_thumbnail(self):
        if self.content_type == self.VIDEO and self.file:
            video_path = self.file.path
            thumbnail_path = os.path.splitext(video_path)[0] + '_thumbnail.jpg'

            generate_thumbnail_from_video(video_path, thumbnail_path)

            with open(thumbnail_path, 'rb') as f:
                self.thumbnail.save(os.path.basename(thumbnail_path), File(f), save=False)

            os.remove(thumbnail_path)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.thumbnail:
            self.save_thumbnail()


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content_type', 'uploaded_at', 'uploaded_by')
    search_fields = ('title',)
    list_filter = ('content_type', 'categories', 'uploaded_at')
    filter_horizontal = ('tags', 'stars')

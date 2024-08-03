from django.urls import path

from .views import *

urlpatterns = [
    path('videos/', videos_view, name='videos'),
    path('music/', music_view, name='music'),
]
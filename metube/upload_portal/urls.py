from django.urls import path

from .views import *

urlpatterns = [
    path('upload/', upload_view, name='upload'),
    path('category/', category_view, name='category'),
    path('star/', star_view, name='star'),
    path('tag/', tag_view, name='tag'),
]
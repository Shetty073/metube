from django.contrib import admin

from .models import Category, CategoryAdmin
from .models import Tag, TagAdmin
from .models import Star, StarAdmin
from .models import Content, ContentAdmin
from .models import Comment, CommentAdmin
from .models import Rating, RatingAdmin
from .models import Playlist, PlaylistAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Playlist, PlaylistAdmin)

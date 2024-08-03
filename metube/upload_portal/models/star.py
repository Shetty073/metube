from django.db import models
from django.contrib import admin

from metube.upload_portal.models.tag import Tag


class Star(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='stars', blank=True, null=True)
    tags = models.ManyToManyField(Tag, limit_choices_to={'tag_type': Tag.PERFORMER}, related_name='stars')

    def __str__(self):
        return self.name
    
    def age(self):
        import datetime
        return f"{int((datetime.date.today() - self.date_of_birth).days / 365.25  )} years"

class StarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth')
    search_fields = ('name',)
    list_filter = ('tags',)
    filter_horizontal = ('tags',)
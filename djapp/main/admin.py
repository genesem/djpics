from django.contrib.admin.sites import site
from django.contrib.admin.options import ModelAdmin
from .models import Image, Tag


class ImageAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']


class TagAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'slen')


site.register(Image, ImageAdmin)
site.register(Tag, TagAdmin)

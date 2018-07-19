
from django.contrib.admin.sites import site
from django.contrib.admin.options import ModelAdmin
from .models import Image


# class PageAdmin(ModelAdmin):
#     list_display = ('slug', 'updated')
#     list_filter = ('updated',)
#     prepopulated_fields = {'slug': ('name',)}


class ImageAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']


# site.register(Page, PageAdmin)
site.register(Image, ImageAdmin)

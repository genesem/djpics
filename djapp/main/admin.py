# admin reference
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/


from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'updated')
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('name',)}



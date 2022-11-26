from django.contrib import admin
from .models import *


class WomenADmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


class ComentAdmin(admin.ModelAdmin):
    list_display = ('text', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Women, WomenADmin)
admin.site.register(Coment, ComentAdmin)

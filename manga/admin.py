from django.contrib import admin
from .models import Manga


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters')

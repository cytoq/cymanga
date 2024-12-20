from django.contrib import admin
from .models import Manga, Comment, Rating


class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'status', 'cover_image_thumbnail', 'average_rating')
    list_filter = ('status', 'genre')
    search_fields = ('title', 'author')
    ordering = ['title']

    def cover_image_thumbnail(self, obj):
        if obj.cover_image:
            return f'<img src="{obj.cover_image.url}" width="50" height="50"/>'
        return "No Image"
    cover_image_thumbnail.allow_tags = True

    def average_rating(self, obj):
        return obj.average_rating() or 'No ratings yet'
    average_rating.admin_order_field = 'average_rating'


admin.site.register(Manga, MangaAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'manga', 'created_at', 'updated_at')
    list_filter = ('created_at', 'manga')
    search_fields = ('user__username', 'manga__title', 'content')
    ordering = ('-created_at',)


admin.site.register(Comment, CommentAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'manga', 'rating')
    list_filter = ('rating', 'manga')
    search_fields = ('user__username', 'manga__title')


admin.site.register(Rating, RatingAdmin)

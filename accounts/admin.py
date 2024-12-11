from django.contrib import admin
from .models import Profile


# Customizing the Profile Model Admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_thumbnail', 'user_role')  # Display user, profile image thumbnail, and role
    search_fields = ('user__username',)  # Search by the user's username
    list_filter = ('user__is_active', 'user__is_staff', 'user__is_superuser')  # Filter by active status and role
    ordering = ('user__username',)  # Order profiles alphabetically by username

    # Method to display the profile image as a thumbnail
    def image_thumbnail(self, obj):
        if obj.image:
            # Return an HTML image tag to display a thumbnail
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />'
        return "No Image"

    # Allow HTML in the 'image_thumbnail' method
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Profile Image'

    # Method to display the user's role
    def user_role(self, obj):
        if obj.user.is_superuser:
            return 'Superuser'
        elif obj.user.is_staff:
            return 'Moderator'
        else:
            return 'Normal User'

    user_role.short_description = 'Role'  # Customizing the column header for the role field


# Register Profile Model with the admin customization
admin.site.register(Profile, ProfileAdmin)

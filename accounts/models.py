from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # One-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Optional profile image with a default image if not set
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[('Publishing', 'Publishing'), ('Finished', 'Finished')]
    )
    chapters_read = models.IntegerField(default=0)
    total_chapters = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='manga_covers/', null=True, blank=True)  # Add this field

    def __str__(self):
        return self.title

    def get_comments(self):
        # Method to get all comments related to this manga
        return self.comments.all()

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return ratings.aggregate(models.Avg('rating'))['rating__avg']
        return None


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comments')  # Use related_name to access comments from Manga
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.manga.title}"


class Rating(models.Model):
    manga = models.ForeignKey(Manga, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars

    def __str__(self):
        return f'{self.user.username} rated {self.manga.title} {self.rating}/5'

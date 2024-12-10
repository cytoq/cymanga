from django.db import models


class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])
    chapters_read = models.IntegerField(default=0)
    total_chapters = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='manga_covers/', null=True, blank=True)  # Add this field

    def __str__(self):
        return self.title

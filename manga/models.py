from django.db import models


class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('reading', 'Reading'), ('completed', 'Completed'), ('plan_to_read', 'Plan to Read')])
    chapters_read = models.IntegerField(default=0)
    total_chapters = models.IntegerField(default=0, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

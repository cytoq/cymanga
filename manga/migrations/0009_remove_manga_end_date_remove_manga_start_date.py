# Generated by Django 5.1.3 on 2024-12-20 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0008_remove_manga_chapters_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='start_date',
        ),
    ]
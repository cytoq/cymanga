# Generated by Django 5.1.3 on 2024-12-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0005_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]

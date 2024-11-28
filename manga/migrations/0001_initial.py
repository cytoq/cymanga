# Generated by Django 5.1.3 on 2024-11-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('reading', 'Reading'), ('completed', 'Completed'), ('plan_to_read', 'Plan to Read')], max_length=50)),
                ('chapters_read', models.IntegerField(default=0)),
                ('total_chapters', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
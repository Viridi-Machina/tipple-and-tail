# Generated by Django 5.0.6 on 2024-06-29 11:33

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_event_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-08 15:16

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_content_alter_page_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
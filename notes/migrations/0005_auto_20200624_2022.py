# Generated by Django 3.0.6 on 2020-06-24 17:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20200624_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]

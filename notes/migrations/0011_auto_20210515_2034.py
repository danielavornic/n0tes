# Generated by Django 3.1.5 on 2021-05-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20210514_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]

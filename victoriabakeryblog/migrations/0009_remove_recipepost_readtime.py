# Generated by Django 3.2.19 on 2023-05-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('victoriabakeryblog', '0008_remove_recipepost_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipepost',
            name='readtime',
        ),
    ]

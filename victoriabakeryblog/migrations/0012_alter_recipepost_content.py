# Generated by Django 3.2.19 on 2023-05-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victoriabakeryblog', '0011_rename_excerpt_recipepost_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepost',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2.18 on 2023-05-03 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('victoriabakeryblog', '0002_auto_20230502_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='thumb_down',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='thumb_up',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserComments',
        ),
        migrations.AddField(
            model_name='usercomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='victoriabakeryblog.recipepost'),
        ),
    ]
# Generated by Django 4.0.6 on 2023-02-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0033_posts_mediatype_alter_posts_file_alter_story_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='mediatype',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-12-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0002_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

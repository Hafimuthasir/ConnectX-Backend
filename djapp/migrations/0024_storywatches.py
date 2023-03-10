# Generated by Django 4.0.6 on 2023-01-03 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0023_alter_posts_downloadscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryWatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djapp.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

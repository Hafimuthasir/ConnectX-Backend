# Generated by Django 4.0.6 on 2022-12-24 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0018_alter_posts_discount_price_alter_posts_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumPurchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='djapp.posts')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

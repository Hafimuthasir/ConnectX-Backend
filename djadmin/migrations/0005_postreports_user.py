# Generated by Django 4.0.6 on 2023-02-04 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djadmin', '0004_alter_bussinessrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='postreports',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

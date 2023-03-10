# Generated by Django 4.0.6 on 2023-02-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0032_alter_storywatches_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='mediatype',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='file',
            field=models.FileField(upload_to='media/posts'),
        ),
        migrations.AlterField(
            model_name='story',
            name='file',
            field=models.FileField(upload_to='media/stories'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.FileField(null=True, upload_to='media/profile'),
        ),
    ]

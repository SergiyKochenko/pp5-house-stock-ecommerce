# Generated by Django 3.2 on 2023-05-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='media'),
        ),
    ]

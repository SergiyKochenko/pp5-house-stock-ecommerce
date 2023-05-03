# Generated by Django 3.2 on 2023-05-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
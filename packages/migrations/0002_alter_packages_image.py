# Generated by Django 3.2 on 2023-04-25 16:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/djck2eqxo/image/upload/v1677807568/no_package_image_mskcnk.webp', max_length=255, verbose_name='Package Image'),
        ),
    ]

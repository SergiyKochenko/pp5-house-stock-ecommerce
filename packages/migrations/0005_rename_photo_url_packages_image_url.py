# Generated by Django 3.2 on 2023-04-25 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_auto_20230425_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='photo_url',
            new_name='image_url',
        ),
    ]
# Generated by Django 3.2 on 2023-05-02 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_userprofile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-06 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='features',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='hashtag',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='long_description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='usecase',
        ),
    ]

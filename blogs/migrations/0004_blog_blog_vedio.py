# Generated by Django 4.2.4 on 2023-09-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_conclusion_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_vedio',
            field=models.FileField(blank=True, upload_to='media/vedio'),
        ),
    ]
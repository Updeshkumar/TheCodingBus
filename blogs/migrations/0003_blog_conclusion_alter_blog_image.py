# Generated by Django 4.2.4 on 2023-09-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_blog_features_remove_blog_hashtag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Conclusion',
            field=models.TextField(default='HELLO TCB'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]

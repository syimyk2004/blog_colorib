# Generated by Django 4.1.5 on 2023-01-11 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_hashtag_category_hashtag_hashtag_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Hashtag',
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='category',
        ),
    ]

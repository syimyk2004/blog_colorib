# Generated by Django 4.1.5 on 2023-01-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(related_name='blogs', to='blog.category'),
        ),
    ]

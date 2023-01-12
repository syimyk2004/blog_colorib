from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Category(models.Model):
    title  = models.CharField(max_length=200)

    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='blogs')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Hashtag = models.ManyToManyField('Hashtag', related_name='Hashtags')


class Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Blog')

class Hashtag(models.Model):
    title = models.CharField(max_length=200)


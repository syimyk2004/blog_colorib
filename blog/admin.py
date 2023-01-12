from django.contrib import admin

# Register your models here.
from .models import Category, Image, Blog, Hashtag

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(Hashtag)
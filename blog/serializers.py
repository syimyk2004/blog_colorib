from rest_framework import serializers
from blog.models import Blog
from blog.models import Category
from blog.models import Hashtag

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog 
        exclude = ('author', 'update_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = instance.blogs.count()
        return representation


class HastagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
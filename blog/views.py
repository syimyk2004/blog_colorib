from rest_framework import generics
from blog.models import Category
from blog.models import Blog
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import CategorySerializer, HastagSerializer, BlogSerializer
from django.db.models import Q
from blog.pagination import BlogListPagination
from blog.models import Hashtag
from rest_framework.response import Response

class BlogListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = BlogListPagination
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_queryset(self):
        search = self.request.query_params.get('search')
        queryset = Blog.objects.all()
        if search:
            queryset = queryset.filter(Q(title__icontains=search)  |
                                       Q(description__icontains=search) |
                                       Q(category__title__icontains=search))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BLogUpdateDeleteGetAPIView(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HashtagListAPIView(generics.ListAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HastagSerializer


class HashtagBlogCategoryListAPIView(generics.ListAPIView):
    def get(self, request, pk):
        quereset = Hashtag.objects.get(id=pk)
    
        serializer = BlogSerializer(quereset.Hashtags.all(), many=True)
        return Response(serializer.data)
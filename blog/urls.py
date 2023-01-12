from django.urls import path 
from . import views

urlpatterns = [
    path('blogs/', views.BlogListCreateAPIView.as_view()),
    path('blogs/<int:pk>/', views.BLogUpdateDeleteGetAPIView.as_view()),
    path('categories/', views.CategoryListAPIView.as_view()),
    path('hastags/', views.HashtagListAPIView.as_view()),
    path('hastags/<int:pk>/', views.HashtagBlogCategoryListAPIView.as_view())
]
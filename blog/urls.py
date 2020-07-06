from django.urls import path
from .views import BlogListView, BlogDetailView, CreateBlog, UpdateBlog, DeleteBlog


urlpatterns=[
    path('', BlogListView.as_view(), name='home'),
    path('blogpost/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blogpost/new/', CreateBlog.as_view(), name='new_post'),
    path('blogpost/<int:pk>/edit/', UpdateBlog.as_view(), name='edit_post'),
    path('blogpost/<int:pk>/delete/', DeleteBlog.as_view(), name='delete_post'),




    ]

from . import views
from django.urls import path
from .views import BlogPost, BlogDetail

urlpatterns = [
    path("", BlogPost.as_view(), name="home"),
    path('<slug:slug>/', BlogDetail.as_view(), name="blog_details"),
]
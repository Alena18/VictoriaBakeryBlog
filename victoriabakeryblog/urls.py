from . import views
from django.urls import path, include
from .views import BlogPost, BlogDetail
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('<slug:slug>/', BlogDetail.as_view(), name='blog_details'),    
    path('recipes.html', BlogPost.as_view(), name='recipes'),
    path('tips.html', views.tips, name='tips'),
    path('sign_up.html', views.sign_up, name='sign_up'),
    path('sign_upconfirm.html', views.confirm, name='confirm'),
    path('connect.html', views.connect, name='connect'),
]
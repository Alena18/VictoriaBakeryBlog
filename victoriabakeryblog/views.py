from django.shortcuts import render
from django.views import generic
from .models import RecipePost

class PostList(generic.ListView):
    model = RecipePost
    queryset = RecipePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


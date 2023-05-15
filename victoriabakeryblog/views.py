from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView
from .models import RecipePost
from django.http import HttpResponse
from .forms import UserCommentForm

class BlogPost(generic.ListView):

    model = RecipePost
    queryset = RecipePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 4

class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = RecipePost.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by("-created_on")
        thumb_up = False
        if blog.thumb_up.filter(id=self.request.user.id).exists():
            thumb_up = True

        return render(
            request,
            "blog_details.html",
            {
                "post": post,
                "comments": comment,
                "thumb_up": thumb_up,
                "comment_form": UserCommentForm()
            },
        )
    def blog_details(request, id):
       blog_details = get_object_or_404(Post, id=id)
       context = {
          'blog_details': blog_details,
           }
       return render(request, 'blog_details.html', context)



def index (request):
    return render(request,'index.html')

def recipes (request):
    return render(request,'recipes.html')

def tips (request):
    return render(request,'tips.html')

def sign_up (request):
    return render(request,'sign_up.html')

def confirm (request):
    return render(request,'sign_upconfirm.html')

def connect (request):
    return render(request,'connect.html')

def askconfirm (request):
    return render(request,'askconfirm.html')

def blog_details (request):
    return render(request, 'blog_details.html')

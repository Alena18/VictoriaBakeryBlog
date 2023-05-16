from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, DetailView
from .models import RecipePost
from django.http import HttpResponse, HttpResponseRedirect
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
        thumb_down = False
        if blog.thumb_down.filter(id=self.request.user.id).exists():
            thumb_down = True    

        return render(
            request,
            "blog_details.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "comment_form": UserCommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = RecipePost.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by("-created_on")
        thumb_up = False
        if blog.thumb_up.filter(id=self.request.user.id).exists():
            thumb_up = True
        thumb_down = False
        if blog.thumb_down.filter(id=self.request.user.id).exists():
            thumb_down = True
            
        comment_form = UserCommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()
        else:
            comment_form = UserCommentForm()

        return render(
            request,
            "blog_details.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "disliked": disliked,
                "comment_form": UserCommentForm()
            },
        )
        
    def blog_details(request, id):
       blog_details = get_object_or_404(Post, id=id)
       context = {
          'blog_details': blog_details,
           }
       return render(request, 'blog_details.html', context)

class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Post, slug=slug)
        if blog.thumb_up.filter(id=request.user.id).exists():
            blog.thumb_up.remove(request.user)
        else:
            blog.thumb_up.add(request.user)

        return HttpResponseRedirect(reverse('blog_details', args=[slug]))

class PostDisLike(View):

    def post(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Post, slug=slug)
        if blog.thumb_down.filter(id=request.user.id).exists():
            blog.thumb_down.remove(request.user)
        else:
            blog.thumb_down.add(request.user)

        return HttpResponseRedirect(reverse('blog_details', args=[slug]))


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

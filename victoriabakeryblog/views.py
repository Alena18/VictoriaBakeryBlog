from django.shortcuts import render
from django.views import generic, View
from django.views.generic import ListView, DetailView
from .models import RecipePost

class BlogPost(generic.ListView):
    model = RecipePost
    queryset = RecipePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        thumb_up = False
        if bog.thumb_up.filter(id=self.request.user.id).exists():
            thumb_up = True

        return render(
            request,
            "blog_details.html",
            {
                "post": post,
                "comments": comment,
                "thumb_up": thumb_up
            },
        )
import readtime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0,"Draft"), (1, "Published"))

class RecipePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    # rate = models.IntegerField(default=0) #related_name='blogpost_rate',
    read_time = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)    
    status = models.IntegerField(choices=STATUS, default=0)
    # thumb_up = models.IntegerField(default=0)
    # thumb_down = models.IntegerField(default=0)

    def read_time(self):
      result = readtime.of_text(self.content)
      return result.text

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class UserComment(models.Model):
    blog = models.ForeignKey(RecipePost, on_delete=models.CASCADE,
                             related_name="comment")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

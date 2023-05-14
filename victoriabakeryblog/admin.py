from django.contrib import admin
from .models import RecipePost, UserComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RecipePost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'updated_on', 'read_time')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(UserComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)

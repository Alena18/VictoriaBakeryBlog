from .models import UserComment
from django import forms


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('body',)

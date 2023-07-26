from django import forms

from .models import Comment


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        exclude = ['created', 'updated', 'approved', 'post']
 
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """ Comment Form """

    class Meta:
        model = Comment
        fields = ('text',)

from django import forms

from .models import Video


class AddVideoForm(forms.ModelForm):
    """ Add video """

    preview = forms.FileField(widget=forms.FileInput, label='Preview', required=True)
    file = forms.FileField(widget=forms.FileInput, label='Video')

    class Meta:
        model = Video
        fields = ('category', 'title', 'slug', 'description', 'preview', 'file')


class EditVideoForm(forms.ModelForm):
    """ Edit video """

    preview = forms.FileField(widget=forms.FileInput, label='Preview', required=True)
    file = forms.FileField(widget=forms.FileInput, label='Video')

    class Meta:
        model = Video
        fields = ('category', 'title', 'slug', 'description', 'preview', 'file')

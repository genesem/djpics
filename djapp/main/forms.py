from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'title', 'desc', 'tags')
        widgets = {
            'url': forms.HiddenInput,
        }
    title = forms.CharField(max_length=200)
    image = forms.ImageField()


class ImageEditForm(forms.ModelForm):
    # title = forms.CharField(max_length=200)
    # image = forms.ImageField()
    class Meta:
        model = Image
        fields = ('title', 'desc', 'tags')
        widgets = {
            'url': forms.HiddenInput,
        }

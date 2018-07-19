from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'title', 'desc')
        widgets = {
            'url': forms.HiddenInput,
        }
    title = forms.CharField(max_length=200)
    image = forms.ImageField()


class ImageEditForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'desc', 'shooted', 'tags')
        widgets = {
            'url': forms.HiddenInput,
        }

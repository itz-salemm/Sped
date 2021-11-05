from django import forms
from django.forms import ModelForm

from .models import *



class UploadFileForm(ModelForm):
    file = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "file",
        "placeholder": "Your Name..",
        "id": "uploadFile"
    }))

    class Meta:
        model = FileText
        fields = ['file']


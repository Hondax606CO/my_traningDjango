from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['name', 'text', 'email']
        widgets = {
            'text': forms.TextInput(attrs={'cols': 200, 'rows': 100})
        }


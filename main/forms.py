# dwitter/forms.py

from django import forms
from .models import *

class DweetForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("user", )

class DweetForm2(forms.ModelForm):
    class Meta:
        model = Javob
        exclude = ('comments',)
        fields = '__all__'
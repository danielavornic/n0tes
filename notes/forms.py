from django import forms
from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'important']
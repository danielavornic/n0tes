from django import forms
from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Untitled'}))
    class Meta:
        model = Note
        fields = ['important', 'title', 'text' ]
    
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
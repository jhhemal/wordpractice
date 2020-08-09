from django import forms
from .models import Word

class WordCreationForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'meaning', 'sentance']

        widgets = {
            'word' : forms.TextInput(attrs={
                'placeholder' : 'Enter Word Name'
            }),
            'meaning' : forms.TextInput(attrs={
                'placeholder' : 'Enter Word Meaning'
            }),
            'sentance' : forms.Textarea(attrs={
                'placeholder' : 'Enter A sentance',
                'rows' : 3
            })
        }

        labels = {
            'word' : "",
            'meaning' : "",
            'sentance' : ""
        }
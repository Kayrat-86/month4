from django import forms
from .models import Film, Comment

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'image', 'genre', 'rating']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


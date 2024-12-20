from django import forms
from django.core.exceptions import ValidationError

from .models import Comment, Manga, Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'genre', 'status', 'total_chapters', 'cover_image']

    def clean_total_chapters(self):
        total_chapters = self.cleaned_data.get('total_chapters')

        if total_chapters <= 0:
            raise ValidationError("Total chapters must be a positive number greater than zero.")

        return total_chapters

    def clean_genre(self):
        genre = self.cleaned_data.get('genre')
        valid_genres = ["Action", "Adventure", "Award Winning", "Comedy", "Supernatural"]

        if genre not in valid_genres:
            raise ValidationError(f"Genre must be one of the following: {', '.join(valid_genres)}.")

        return genre


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search Manga")


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    rating = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], widget=forms.Select(attrs={'class': 'form-control'}))

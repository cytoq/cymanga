from django import forms
from .models import Comment, Manga, Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters', 'start_date', 'end_date', 'cover_image']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search Manga")


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']  # Only include the rating field

    rating = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], widget=forms.Select(attrs={'class': 'form-control'}))

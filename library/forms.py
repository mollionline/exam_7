from django import forms
from library.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book', 'description', 'author', 'published_at']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=False)
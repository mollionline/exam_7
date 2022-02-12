from django import forms
from library.models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book', 'description', 'published_at']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author', 'birthday', 'death_date', 'description']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=False)


class BookWithoutAuthorForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book', 'description', 'published_at', 'author']

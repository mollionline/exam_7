from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from library.helpers import SearchView
from library.models import Book, Author
from library.forms import BookForm, SearchForm, AuthorForm


class ListAuthorView(SearchView):
    template_name = 'author/list_author.html'
    model = Author
    ordering = ('author',)
    paginate_by = 5
    context_object_name = 'authors'
    search_form = SearchForm
    search_fields = {
        'author': 'icontains'
    }


class DetailAuthorView(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = 'author/detail_author.html'

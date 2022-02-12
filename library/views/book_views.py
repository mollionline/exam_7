from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from library.helpers import SearchView
from library.models import Book
from library.forms import BookForm, SearchForm


class ListBookView(SearchView):
    template_name = 'book/list_book.html'
    model = Book
    ordering = ('book',)
    paginate_by = 5
    context_object_name = 'books'
    search_form = SearchForm
    search_fields = {
        'book': 'startswith'
    }


class DetailBookView(DetailView):
    context_object_name = 'book'
    model = Book
    template_name = 'book/detail_book.html'


class CreateBookView(CreateView):
    model = Book
    template_name = 'book/create_book.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('detail_book', kwargs={'pk': self.object.pk})


class UpdateBookView(UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('detail_book', kwargs={'pk': self.get_object().pk})


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('list_book')

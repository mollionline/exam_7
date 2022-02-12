from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from library.helpers import SearchView
from library.models import Book, Author, Genre
from library.forms import BookForm, SearchForm, BookWithoutAuthorForm


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
    form_class = BookForm
    template_name = 'author/detail_author.html'

    def get_success_url(self):
        return reverse('detail_author', kwargs={'pk': self.kwargs.get('pk')})

    def post(self, request, *args, **kwargs):
        author_pk = kwargs.get('pk')
        author = get_object_or_404(Author, pk=author_pk)
        form = self.form_class(data=request.POST)
        if form.is_valid():
            genre = form.cleaned_data.get('genre')
            book, is_not_new = Book.objects.get_or_create(
                book=form.cleaned_data.get('book'),
                description=form.cleaned_data.get('description'),
                published_at=form.cleaned_data.get('published_at'),
                author=author
            )
            book.genre.set(genre)
            return redirect(self.get_success_url())
        return render(request, self.template_name, context={
            'author': author,
            'form': form,
            'genres': Genre.objects.all()
        })


class UpdateBookView(UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('detail_author', kwargs={'pk': self.object.author.pk})


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('list_book')


class CreateBookWithAuthor(CreateView):
    model = Book
    form_class = BookWithoutAuthorForm
    template_name = 'book/create_book.html'

    def get_success_url(self):
        return reverse('detail_author', kwargs={'pk': self.object.author.pk})

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import CreateView, ListView


from library.models import Genre


class CreateGenreView(CreateView):
    model = Genre
    template_name = 'genre/create_genre.html'
    fields = ['genre']
    success_url = '/genres/'


class ListGenreView(ListView):
    template_name = 'genre/list_genre.html'
    model = Genre
    ordering = ('genre',)
    context_object_name = 'genres'


def genre_delete_view(request, pk):
    try:
        category = Genre.objects.get(pk=pk)
        category.delete()
        return HttpResponseRedirect('/genres/')
    except Genre.DoesNotExist:
        return HttpResponseNotFound("<h2>Genre not found</h2>")


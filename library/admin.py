from django.contrib import admin
from library.models import Book, Author


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'birthday', 'death_date', 'description']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['id', 'author', 'birthday', 'death_date', 'description']
    readonly_fields = ['id']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'description', 'author', 'published_at']
    list_filter = ['book']
    search_fields = ['book']
    fields = ['id', 'book', 'description', 'author', 'published_at']
    readonly_fields = ['id']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

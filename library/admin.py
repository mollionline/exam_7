from django.contrib import admin
from library.models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'description', 'author', 'published_at']
    list_filter = ['book']
    search_fields = ['book']
    fields = ['id', 'book', 'description', 'author', 'published_at']
    readonly_fields = ['id']


admin.site.register(Book, BookAdmin)

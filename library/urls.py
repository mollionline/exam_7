from django.urls import path
from library.views.author_views import (ListAuthorView,
                                        DetailAuthorView)

from library.views.book_views import (ListBookView,
                                      DetailBookView,
                                      CreateBookView,
                                      UpdateBookView,
                                      DeleteBookView,
                                      CreateBookWithAuthor)

urlpatterns = []

author_urls = [
    path('authors/<int:pk>/', DetailAuthorView.as_view(), name='detail_author'),
    path('authors/', ListAuthorView.as_view(), name='list_author')
]

book_urls = [
    path('authors/<int:pk>/book', CreateBookView.as_view(), name='create_book'),
    path('', ListBookView.as_view(), name='list_book'),
    path('books/<int:pk>/', DetailBookView.as_view(), name='detail_book'),
    path('books/<int:pk>/delete', DeleteBookView.as_view(), name='delete_book'),
    path('books/<int:pk>/edit', UpdateBookView.as_view(), name='update_book'),
    path('authors/book/create', CreateBookWithAuthor.as_view(), name='create_book_without_author')
]

urlpatterns += author_urls
urlpatterns += book_urls

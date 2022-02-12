from django.urls import path
from library.views.book_views import (ListBookView,
                                      DetailBookView,
                                      CreateBookView,
                                      UpdateBookView,
                                      DeleteBookView)

urlpatterns = []

book_urls = [
    path('', ListBookView.as_view(), name='list_book'),
    path('books/add/', CreateBookView.as_view(), name='create_book'),
    path('books/<int:pk>/', DetailBookView.as_view(), name='detail_book'),
    path('books/<int:pk>/delete', DeleteBookView.as_view(), name='delete_book'),
    path('books/<int:pk>/edit', UpdateBookView.as_view(), name='update_book')
]

urlpatterns += book_urls

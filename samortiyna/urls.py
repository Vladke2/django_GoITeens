from django.urls import path
from views import add_book, book_list, search_book

urlpatterns = [
    path('addbook/', add_book),
    path('booklist/', book_list),
    path('searchbook/', search_book)
]
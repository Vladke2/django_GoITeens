from django.shortcuts import render
from forms import AddBook
from models import Book


def add_book(request):
    if request.method == 'POST':
        form = AddBook()
        if form.is_valid():
            form.save()
    else:
        form = AddBook()
        return render(request, 'html.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render('html2.html', {'books': books})


def search_book(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render('html3.html', {'books': books})

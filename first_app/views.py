from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Author, Book, Comments, Publisher, Store


def main_page(request):
    return render(request, 'first_app/main.html')


def show_authors(request):
    authors = Author.objects.order_by('id')
    return render(request, 'first_app/authors.html', {'authors': authors})


def stores(request):
    store = Store.objects.order_by('id')
    return render(request, 'first_app/stores.html', {'store': store})


def publishers(request):
    publisher = Publisher.objects.order_by('id')
    return render(request, 'first_app/publishers.html', {'publisher': publisher})


def show_store(request, id):
    store = get_object_or_404(Store, id=id)
    return render(request, 'first_app/store.html', {'store': store})


def show_books(request):
    book = Book.objects.order_by('-pubdate')
    return render(request, 'first_app/show_books.html', {'book': book})


def show_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'first_app/book.html', {'book': book})


# class BookInstanceDetailView(DetailView):
#     model = Book
#     template_name = 'first_app/book.html'
#     context_object_name = 'book'


def show_comments(request):
    comment = Book.objects.order_by('-pubdate')
    return render(request, 'first_app/index.html', {'comment': comment})


def show_author(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'first_app/show_author.html', {'author': author})


# class ShowAuthor(DetailView):
#     model = Author
#     template_name = 'first_app/index.html'
#     context_object_name = 'author'
#     fields = ['name', 'age']

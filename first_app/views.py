from django.shortcuts import get_object_or_404, render
from django.db.models import Avg, Count
from .models import Author, Book, Comments, Publisher, Store


def tofixed(numobj, digits=0):
    return f"{numobj:.{digits}f}"


def main_page(request):
    return render(request, 'first_app/main.html')


def show_authors(request):
    authors = Author.objects.order_by('id')
    count = Author.objects.annotate(num_books=Count('name')).count
    age = Author.objects.all().aggregate(Avg('age'))['age__avg']
    if authors and count and age:
        return render(request, 'first_app/authors.html', {'authors': authors,
                                                          'count': count,
                                                          'age': tofixed(age, 2)})
    else:
        return render(request, 'first_app/authors.html', {})


def show_author(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'first_app/show_author.html', {'author': author})


def stores(request):
    store = Store.objects.order_by('id')
    count = Store.objects.annotate(num_books=Count('name')).count
    return render(request, 'first_app/stores.html', {'store': store,
                                                     'count': count, })


def show_store(request, id):
    store = get_object_or_404(Store, id=id)
    return render(request, 'first_app/store.html', {'store': store})


def publishers(request):
    publisher = Book.objects.order_by('id')
    count = Publisher.objects.annotate(num_books=Count('name')).count
    return render(request, 'first_app/publishers.html', {'publisher': publisher,
                                                         'count': count, })


def show_publisher(request, id):
    publisher = get_object_or_404(Book, id=id)
    return render(request, 'first_app/publisher.html', {'publisher': publisher})


def show_books(request):
    book = Book.objects.order_by('-pubdate')
    price = Book.objects.all().aggregate(Avg('price'))['price__avg']
    rating = Book.objects.all().aggregate(Avg('rating'))['rating__avg']
    pubs = Book.objects.annotate(num_books=Count('name')).count
    if price and rating and pubs:
        return render(request, 'first_app/show_books.html', {'book': book,
                                                             'price': tofixed(price, 2),
                                                             'rating': tofixed(rating, 2),
                                                             'pubs': pubs})
    else:
        return render(request, 'first_app/show_books.html', {})


def show_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'first_app/book.html', {'book': book})


def show_comments(request):
    comment = Book.objects.order_by('-pubdate')
    count = Comments.objects.annotate(num_books=Count('comment')).count
    return render(request, 'first_app/index.html', {'comment': comment,
                                                    'count': count})


def show_comment(request, id):
    comment = get_object_or_404(Book, id=id)
    return render(request, 'first_app/show_comment.html', {'comment': comment})


from django.urls import path

from . import views

app_name = 'first_app'
urlpatterns = [
    path('comments/', views.show_comments, name='comments'),
    path('authors/', views.show_authors, name='authors'),
    path('authors/<int:id>', views.show_author, name='author'),
    path('books/', views.show_books, name='books'),
    path('', views.main_page, name='main'),
    path('books/<int:id>', views.show_book, name='book-instance'),
    path('stores/<int:id>', views.show_store, name='store'),
    path('comments/<int:id>', views.show_comment, name='comment'),
    path('publishers/<int:id>', views.show_publisher, name='publisher'),
    path('stores/', views.stores, name='stores'),
    path('publishers/', views.publishers, name='publishers'),

]

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Author'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.CharField(max_length=1000, unique=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.comment


class Book(models.Model):
    name = models.CharField(max_length=300, null=True)
    pages = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rating = models.FloatField(null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, to_field='name', default=None)
    pubdate = models.DateField(null=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, to_field='comment', default=None)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def display_authors(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([authors.name for authors in self.authors.all()[:3]])

    display_authors.short_description = 'Authors'


class Store(models.Model):
    name = models.CharField(max_length=300, null=True)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def display_books(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([books.name for books in self.books.all()[:3]])

    display_books.short_description = 'Books'

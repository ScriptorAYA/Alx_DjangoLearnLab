from django.db import models


class Author(models.Model):
    """
    Author Model

    Represents a book author.
    Each author can have multiple books (one-to-many relationship).
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book Model

    Represents a book written by an author.

    Fields:
    - title: Name of the book.
    - publication_year: Year the book was published.
    - author: ForeignKey linking the book to its Author.
    """

    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    # One-to-many relationship:
    # One Author → Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

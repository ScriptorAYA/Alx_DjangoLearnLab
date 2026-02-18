from django.db import models

# ------------------------------------------------------------
# Author Model
# ------------------------------------------------------------
# Represents a book author.
# One author can have multiple books (one-to-many relationship).
# ------------------------------------------------------------

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ------------------------------------------------------------
# Book Model
# ------------------------------------------------------------
# Represents a book written by an Author.
# Each Book belongs to one Author via a ForeignKey.
# The related_name='books' allows reverse access:
# author.books.all()
# ------------------------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # Establishes one-to-many relationship:
    # One Author → Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


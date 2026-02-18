from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer

    Serializes all fields of the Book model.

    Custom Validation:
    Ensures publication_year is not set in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom field validation to prevent future publication years.
        """
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )

        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer

    Serializes the Author model.

    Includes nested serialization of related books using
    BookSerializer.

    Relationship Handling:
    - The 'books' field uses the related_name defined in the Book model.
    - many=True indicates one author can have multiple books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']


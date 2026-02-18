from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


# ------------------------------------------------------------
# BookSerializer
# ------------------------------------------------------------
# Serializes all fields of the Book model.
# Includes custom validation to ensure publication_year
# is not set in the future.
# ------------------------------------------------------------

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# ------------------------------------------------------------
# AuthorSerializer
# ------------------------------------------------------------
# Serializes Author data.
# Includes nested BookSerializer to dynamically
# display all related books.
#
# Uses the related_name='books' from the Book model.
# many=True because an author can have multiple books.
# read_only=True prevents nested creation conflicts.
# ------------------------------------------------------------

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']


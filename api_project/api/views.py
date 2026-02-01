from rest_framework import generics
from rest_framework import generics as rest_framework_generics
from .models import Book
from .serializers import BookSerializer

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


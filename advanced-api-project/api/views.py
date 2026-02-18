from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer


# ------------------------------------------------------------
# BookListView
# ------------------------------------------------------------
# GET: Retrieve all books
# Public access (read-only)
# ------------------------------------------------------------

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

        # 🔹 Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 🔹 Fields that can be filtered using query params
    filterset_fields = ['title', 'author__name', 'publication_year']

    # 🔹 Fields to search by using ?search=
    search_fields = ['title', 'author__name']

    # 🔹 Fields allowed for ordering using ?ordering=
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # default ordering

"""
BookListView:

- Supports filtering by title, author name, and publication year.
- Supports search by title and author name.
- Supports ordering by title, publication year, or author name.
- Read-only for unauthenticated users; write requires authentication elsewhere.
"""


# ------------------------------------------------------------
# BookDetailView
# ------------------------------------------------------------
# GET: Retrieve a single book by ID
# Public access (read-only)
# ------------------------------------------------------------

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ------------------------------------------------------------
# BookCreateView
# ------------------------------------------------------------
# POST: Create a new book
# Restricted to authenticated users
# ------------------------------------------------------------

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior example
    def perform_create(self, serializer):
        # Additional logic can be added here if needed
        serializer.save()


# ------------------------------------------------------------
# BookUpdateView
# ------------------------------------------------------------
# PUT / PATCH: Update an existing book
# Restricted to authenticated users
# ------------------------------------------------------------

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# ------------------------------------------------------------
# BookDeleteView
# ------------------------------------------------------------
# DELETE: Remove a book
# Restricted to authenticated users
# ------------------------------------------------------------

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


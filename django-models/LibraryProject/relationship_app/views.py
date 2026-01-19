from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # Library must be explicitly imported

# -------------------------
# Function-based view
# -------------------------
def list_books(request):
    """
    Display a simple text list of all books and their authors.
    """
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------
# Class-based view
# -------------------------
class LibraryDetailView(DetailView):
    """
    Display details of a specific library, including all books in it.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"  # Must include app name
    context_object_name = "library"


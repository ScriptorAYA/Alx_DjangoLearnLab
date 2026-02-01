from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Relationship App!")

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/delete_book.html', {'book': book})


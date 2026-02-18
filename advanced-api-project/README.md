# Advanced API Project

## Overview
This project demonstrates the use of Django REST Framework generic views
to implement full CRUD functionality for the Book model.

## Views Implemented

- BookListView → Lists all books (public access)
- BookDetailView → Retrieves a single book (public access)
- BookCreateView → Creates a book (authenticated users only)
- BookUpdateView → Updates a book (authenticated users only)
- BookDeleteView → Deletes a book (authenticated users only)

## Permissions

- Read-only access is allowed for unauthenticated users.
- Write operations require authentication using DRF permission classes.

## Custom Behavior

- perform_create() and perform_update() methods are overridden
  to allow future extensibility.
- BookSerializer validates publication_year to prevent future dates.


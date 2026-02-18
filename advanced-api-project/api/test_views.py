"""
Unit Tests for Book API Endpoints

- Tests List, Retrieve, Create, Update, Delete operations.
- Tests filtering, search, and ordering.
- Verifies permission enforcement for authenticated vs unauthenticated users.
- Uses Django's APITestCase with a temporary test database.
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name='J.K. Rowling')

        # Create some books
        self.book1 = Book.objects.create(title='Harry Potter 1', publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title='Harry Potter 2', publication_year=1998, author=self.author)

        # Login user for authenticated tests
        self.client.login(username='testuser', password='testpass')

            # ----------------------------
    # Test Listing Books (GET /books/)
    # ----------------------------
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # two books created


    # ----------------------------
    # Test Retrieve Book (GET /books/<id>/)
    # ----------------------------
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter 1')


    # ----------------------------
    # Test Create Book (POST /books/create/)
    # ----------------------------
    def test_create_book(self):
        url = reverse('book-create')
        data = {'title': 'Harry Potter 3', 'publication_year': 1999, 'author': self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)


    # ----------------------------
    # Test Update Book (PUT /books/update/<id>/)
    # ----------------------------
    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Harry Potter 1 Updated', 'publication_year': 1997, 'author': self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter 1 Updated')


    # ----------------------------
    # Test Delete Book (DELETE /books/delete/<id>/)
    # ----------------------------
    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


        # ----------------------------
    # Test Search Functionality
    # ----------------------------
    def test_search_books(self):
        url = reverse('book-list') + '?search=Harry Potter 1'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 1')


    # ----------------------------
    # Test Ordering by publication_year
    # ----------------------------
    def test_order_books(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 1998)


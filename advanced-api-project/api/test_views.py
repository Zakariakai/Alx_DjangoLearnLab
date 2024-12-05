# api/test_views.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookTests(APITestCase):

    def setUp(self):
        """Set up a user and a book for testing"""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2020)

    def test_create_book(self):
        """Test creating a book"""
        url = '/api/books/'  # Make sure this is the correct endpoint
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        
        # Test without authentication (should fail)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test with authentication (should succeed)
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Make sure one book was added

    def test_update_book(self):
        """Test updating a book"""
        url = f'/api/books/{self.book.id}/'
        data = {'title': 'Updated Title', 'author': 'Updated Author', 'publication_year': 2021}
        
        # Test without authentication (should fail)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test with authentication (should succeed)
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh to get updated data from the database
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        """Test deleting a book"""
        url = f'/api/books/{self.book.id}/'
        
        # Test without authentication (should fail)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test with authentication (should succeed)
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Make sure the book is deleted

    def test_list_books(self):
        """Test listing books"""
        url = '/api/books/'
        
        # Test without authentication (should succeed)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only 1 book should be returned
        
        # Test with authentication (should still succeed)
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should still be 1 book

    def test_search_books(self):
        """Test search functionality"""
        url = '/api/books/?search=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return the book containing 'Test' in title or author

from django.urls import path
<<<<<<< HEAD
from .views import home, book_new

urlpatterns = [
    path('', home, name='book-list'),
    path('add/book/', book_new , name='book-new')
]
=======
from . import views

urlpatterns = [
    # URL pattern for listing all books
    path('books/', views.book_list, name='book_list'),

    # URL pattern for viewing details of a specific book
    path('books/<int:pk>/', views.book_details, name='book_details'),

    # URL pattern for creating a new book
    path('books/create/', views.create_book, name='create_book'),

    # URL pattern for editing a specific book
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),

    # URL pattern for deleting a specific book
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

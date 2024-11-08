# relationship_app/views.py
from django.shortcuts import render
from django.http import Http404
from django.views import View
from .models import Book, Library, Author

# Function-based view for listing all books
def list_books(request):
    # Get all books from the database
    books = Book.objects.all()
    
    # Render the list_books.html template and pass the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying details of a specific library
class LibraryDetailView(View):
    def get(self, request, library_name):
        try:
            # Get the library by name
            library = Library.objects.get(name=library_name)
        except Library.DoesNotExist:
            raise Http404("Library not found")
        
        # Get all books in the library
        books = library.books.all()
        
        # Render the library_detail.html template and pass the library and books context
        return render(request, 'relationship_app/library_detail.html', {'library': library, 'books': books})

from .models import Book, Library
from django.shortcuts import render
from django.views.generic import DetailView

# Function-based view to list all books
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the books in the 'list_books.html' template
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display a specific library's details
class LibraryDetailView(DetailView):
    # Specify the model for this view
    model = Library
    # The template to be used for rendering
    template_name = 'relationship_app/library_detail.html'
    # The name of the context variable that will contain the library data
    context_object_name = 'library'

    # Optionally, you can override the get_context_data method to add extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context or filter the books here if needed
        return context

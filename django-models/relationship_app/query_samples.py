# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    # Retrieve the author based on the name provided
    author = Author.objects.get(name=author_name)
    # Get all books that belong to this author
    books = Book.objects.filter(author=author)
    
    # Print out the titles of all books by the author
    for book in books:
        print(f"Book: {book.title}")

# List all books in a specific library
def books_in_library(library_name):
    # Retrieve the library based on the name
    library = Library.objects.get(name=library_name)
    # Get all books in that library
    books = library.books.all()
    
    # Print out the titles of all books in that library
    for book in books:
        print(f"Book: {book.title}")

# Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    # Retrieve the library by name
    library = Library.objects.get(name=library_name)
    # Get the librarian for this library (1-to-1 relationship)
    librarian = Librarian.objects.get(library=library)
    
    # Print the librarian's name
    print(f"Librarian: {librarian.name}")

if __name__ == "__main__":
    # Example usage of the queries (replace 'Author Name' and 'Library Name' with actual data)
    books_by_author('Author Name')
    books_in_library('Library Name')
    librarian_for_library('Library Name')


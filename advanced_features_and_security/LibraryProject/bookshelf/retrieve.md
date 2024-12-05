<<<<<<< HEAD
# CRUD Operations - Retrieve: 

## Command Instruction: 
Retrieve and display all attributes of the book you just created.

## Code : 
`>>> a_book = Book.objects.get(id=3)`
`>>> print(a_book)`

## Expected output:
`id: 3
title: 1984
author: George Orwell
publication_year: 1949
`
=======
from bookshelf.models import Book

#Retrieving the books
books = Book.objects.get.all()                                 

#iterating through the records of the books
for book in books:
    print(book.title, book.author, book.publication_year)       

#Expected outcome
1984 George Orwell 1949
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

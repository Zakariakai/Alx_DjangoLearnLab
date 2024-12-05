<<<<<<< HEAD
# CRUD Operations - Update: 

## Command Instruction: 
Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

## Code : 
`>>> a_book.title = "Nineteen Eighty-Four"`
`>>> a_book.save()`
`>>>print(a_book)`

## Expected output:
`id: 3
title: Nineteen Eighty-Four
author: George Orwell
publication_year: 1949
`
=======
from bookshelf.models import Book

book =Book.objects.get(title="1984")

#Updating the book title
book.title = Book.objects.update(title = "Nineteen Eighty-Four") 

#Saving the update
book.save()

#fetching the updated book to confirm if it was successful
updated_book = Book.objects.get(title=book.title)

#Printing the updated_book
print(updated_book)

#Output
Nineteen Eighty-Four by George Orwell (1949)
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

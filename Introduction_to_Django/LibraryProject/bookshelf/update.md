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
<<<<<<< HEAD
# Update books
from bookshelf.models import Book
book = Book.objects.get(title='1984')
book.title="Nineteen Eighty-Four"
book.save()
=======
book.title = "Nineteen Eighty-Four"
book.save()
>>>>>>> origin/master
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

<<<<<<< HEAD
# CRUD Operations - Delete: 

## Command Instruction: 
Delete the book you created and confirm the deletion by trying to retrieve all books again.

## Code : 

#*Code to delete an instance*
`>>> a_book.delete()`


## Expected output:
#*Output after deletion of a book object*
> 'from bookshelf.models import Book'
> `(1, {'bookshelf.Book': 1})
`

#*Output trying to retrieve all book object*

> QuerySet[ 
> Book: id: 1
title: Things fall apart
author: Chinwe Achebe
publication_year: 1959,

> Book: id: 2
title: Rich Dad Poor Dad
author: Robert kiyosaki
publication_year: 2005,

> Book: id: 4
title: Think and grow rich
author: Someone
publication_year: 1997]
=======
#importing Book models
from bookshelf.models import Book

#retriveing the book
book = Book.objects.get(author="George Orwell")

#Deleting the book instnace
book.delete()

#results
(1, {'bookshelf.Book': 1})

#Trying to retrieve all the books and confirm if deletion was #successful
books = Book.objects.get.all()
print(books)
#Output showing an empty list
<QuerySet []>
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

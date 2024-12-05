<<<<<<< HEAD
# All Commands Operations and Output

# Code - Create : 
`>>> a_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`

## Expected output:
`>>> 
#*A new empty prompt signifies a successful creation*`


# Code Update : 
`>>> a_book = Book.objects.get(id=3)`
`>>> print(a_book)`

## Expected output:
`id: 3
title: 1984
author: George Orwell
publication_year: 1949
`

# Code - Update : 
`>>> a_book.title = "Nineteen Eighty-Four"`
`>>> a_book.save()`
`>>>print(a_book)`

## Expected output:
`id: 3
title: Nineteen Eighty-Four
author: George Orwell
publication_year: 1949
`

# Code - Delete: 

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
#CREATING Book Instance
#importing Book models

from bookshelf.models import Book

#Creating a Book instance 

new_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)    

#Saving the added book

new_book.save()

print(new_book)

#Expected output: 

1984 by George Orwell (1949)


#RETRIEVING of the book
from bookshelf.models import Book

#Retrieving the books
books = Book.objects.get.all()                                 

#iterating through the records of the books
for book in books:
    print(book.title, book.author, book.publication_year)       

#Expected outcome
1984 George Orwell 1949


#UPDATING Book instance
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


#DELETING the Book instance
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

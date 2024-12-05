<<<<<<< HEAD
# CRUD Operations - Create: 

## Command Instruction: 
Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

## Code : 
`>>> a_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`

## Expected output:
`>>> 
#*A new empty prompt signifies a successful creation*`
=======
#importing Book models

from bookshelf.models import Book

#Creating a Book instance 

new_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)    

#Saving the added book

new_book.save()

print(new_book)

#Expected output: 

1984 by George Orwell (1949)
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

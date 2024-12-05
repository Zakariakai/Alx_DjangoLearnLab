<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.contrib.auth.models import Permission

# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(verbose_name=("profile picture"), upload_to='profile_image/', null=True)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        
        if not email:
            raise ValueError('The Email field must be set')
        
        # Normalize the email by lowering the domain part.
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        
        # Set password using Django's built-in method to hash the password
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the specified email and password.
        """ 
        # Define default values for is_staff and is_superuser as True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Raise errors if the necessary fields are not set
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
        

  
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    # author is a Foreign key from the author model and can be accessed from the author model as books
    author = models.CharField(max_length=100)
    # IntegerField.
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title     
    
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'can change book'),
            ('can_delete_book', 'can delete book')
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=50)
    # books has a ManytoMany rel. to the Library model and can be accessed from the book model as libraries_found
    books = models.ManyToManyField(Book, related_name='Libraries_found')
    

    def display_books(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(book.title for book in self.books.all()[:3])

    display_books.short_description = 'Books'

    def display_book_count(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return len(self.books.all())

    display_book_count.short_description = 'Count of Books'
    
    def __str__(self):
        return self.name    
    
    class Meta:
        permissions = [
            ('can_view', 'can view'),
            ('can_create', 'can create'),
            ('can_edit', 'can edit'),
            ('can_delete', 'can delete'),
        ]   
        
=======
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from relationship_app.models import Book


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        
        #Validating Email
        if not email:
            raise ValueError('User must have an email address')
        #Fetching and normalizing email
        user = self.model(email=self.normalize_email(email), **extra_fields)

        #Setting password (hashes password)
        user.set_password(password)
        #saving created user in current database
        user.save(using=self._db)
        #returning created user
        return user
    
    #creating superuser ensuring administrative users can be created with the required fields fields
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
#Custom User Model by extending AbstractUser
#from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default='2020-01-01', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField(default = '2020-01-01')
    modified_by = models.ForeignKey()

#Extending Book Model with Custom Permissions
    class Meta:
        permissions =(
            ('can_create', 'Can create'),
            ('can_view', 'Can view'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),

        )

    def __str__(self):
        return f"{self.title} by {self.author} published on {self.publication_date}"



    class Meta:
        permissions = [
            ('can_view', 'Can view'),
            ('can_create', 'Can create'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),
        ]       
          
   
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

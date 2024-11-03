from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the admin list view
    search_fields = ('title', 'author')  # Fields to search in the admin panel
    list_filter = ('publication_year',)  # Fields to filter the list by

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)

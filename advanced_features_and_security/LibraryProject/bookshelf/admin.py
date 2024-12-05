from django.contrib import admin
<<<<<<< HEAD
from .models import Book
from .models import Book, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

# admin.site.register(CustomUser, UserAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email' ,'date_of_birth', 'profile_photo')
    
    
admin.site.register(CustomUser, CustomUserAdmin)
    
=======
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book #Import Book model from models

# Register your models here.

#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author') # Filter books by title and author
    search_fields = ('title', 'author')
                     
admin.site.register(Book, BookAdmin)

#Integrate the Custom User Model into Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('email', 'is_staff', 'date_of_birth', 'username', 'profile_photo')
admin.site.register(CustomUser, CustomUserAdmin)

>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

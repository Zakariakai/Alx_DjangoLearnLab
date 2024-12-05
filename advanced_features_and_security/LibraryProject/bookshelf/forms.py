from django import forms
<<<<<<< HEAD

# Forms are elegate means to add and edit data in our web app

from .models import Book

class ExampleForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year')
        

=======
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
    
    def clean_author(self):
        author = self.cleaned_data['author']
        return author
    
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200) 
    author = forms.CharField(max_length=200)
    publication_date = forms.DateField()
    
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

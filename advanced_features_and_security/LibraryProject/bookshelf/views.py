from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Create your views here.
# @permission_required('app_name.can_edit', raise_exception=True)

@permission_required('bookshelf.can_edit', raise_exception=True)
def home(request):
    all_books = Book.objects.all()
    books = {'books': all_books}
    return render(request, template_name='bookshelf/book_list.html', context= books)

def book_new(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form} )
=======

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import ExampleForm, BookForm
from django.contrib.auth.decorators import permission_required, login_required

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':	
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/edit-book.html', {'form':form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookshelf/book_list.html', {"books":books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book-details.html', {'book':book})


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.updated_by = request.user
            form.save()
            return redirect('book_details', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit-book.html', {'form':form})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/deleted-book.html', {'book':book})

@login_required
def form_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data here
            form.save()  # Or any other processing
            return redirect('success')  # Redirect after successful submission
    else:
        form = ExampleForm()

    return render(request, 'form_example.html', {'form': form})
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

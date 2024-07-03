from django.shortcuts import render
from .models import Author,Book,Book_instance
# Create your views here.

def index(request):

    num_of_books = Book.objects.all().count()
    num_of_author = Author.objects.all().count()
    num_of_book_instance = Book_instance.objects.all().count()

    available_books = Book_instance.objects.filter(status = 'a').count()

    context ={
        'num_of_books': num_of_books,
        'num_of_authors' : num_of_author,
        'num_of_book_instances' : num_of_book_instance,
        'available_books' : available_books
    }

    return render(request,'index.html',context)
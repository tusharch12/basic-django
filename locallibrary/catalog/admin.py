from django.contrib import admin
from .models import Author, Book, Book_instance, Genre
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Book_instance)
admin.site.register(Genre)

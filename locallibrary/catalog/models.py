from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid
from django.urls import reverse 


class Genre(models.Model):
    name = models.CharField(max_length=200,unique=True,help_text = "Enter the Name (eg. Romatic, ficition and non fiction)")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reversed('genre-deatails',args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name = 'genre_name_case_insensitive_unqiue',
                violation_error_message = "Genre already exists (case insensitive match)"
            )
        ]

class Author(models.Model):
    first_name = models.CharField(max_length= 200,)
    last_name = models.CharField(max_length= 200)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died',null = True, blank = True ) 

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'  
    
class Book(models.Model):
    title = models.CharField(max_length = 200,)
    author = models.ForeignKey("Author", on_delete=models.CASCADE,null=True)
    summary = models.TextField(max_length=500 ,help_text= "Enter the summary")

    isbn = models.CharField(max_length = 13 , unique=True)
    language = models.CharField(max_length = 50)
    genre = models.ManyToManyField("Genre",help_text = "Select the genre")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Book_instance(models.Model):
    id = models.UUIDField(primary_key = True,default=uuid.uuid4)  
    book = models.ForeignKey("Book", on_delete = models.RESTRICT,null = True )
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null = True,blank=True)

    LOAN_STATUS = (
        ('m','Maintinace'),
        ('o','On Loan'),
        ('a','Avaiable'),
        ('r','Reserved')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank= True,default='m',help_text='Book Avaiablity')  

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'





    
        


from django.db import models

class MyModalName(models.Model):
    
    my_name= models.CharField(max_length=10,  help_text='Enter the name')

class Genre(models.Model):
    name = models.CharField(max_length=200,unique=True,help_text = "Enter the Name (eg. Romatic, ficition and non fiction)")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reversed('genre-deatails',args=[str(self.id)])

class Author(models.Model):
     first_name = models.CharField(max_length= 200,)
     last_name = models.CharField(max_length= 200)
     date_of_birth = models.DateField(null=True,blank=True)
     date_of_death = models.DateField('Died',null = True, blank = True )   
    
class Book(models.Model):
    title = models.CharField(max_length = 200,)
    author = models.models.ForeignKey("Author", on_delete=models.CASCADE,null=True)
    summary = models.TextField(max_length=500 ,help_text= "Enter the summary")

    isbn = models.CharField(max_length = 13 , unique=True)
    language = models.CharField(max_length = 50)
    genre = mode
        


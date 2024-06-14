from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey(Author,related_name='book', on_delete=models.CASCADE)
    isbn_number=models.IntegerField()
    pages=models.IntegerField()

    def __str__(self):
        return  f"{self.name} {self.author}"



class Student(models.Model):
   full_name=models.CharField(max_length=200)
   roll_no=models.IntegerField()
   grade= models.CharField(max_length=1, blank=True, null=True)
    
   def __str__(self):
        return self.full_name


class Course(models.Model):
    name=models.CharField(max_length=150)
    student=models.ManyToManyField(Student,related_name='course')

    def __str__(self):
        return f"{self.name} {self.student}"

    
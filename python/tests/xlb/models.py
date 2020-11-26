from django.db import models
class Publisher(models.Model):
  name = models.CharField(max_length=30)
  image= models.CharField(max_length=30,null=True)
  
  def __str__(self):
    return self.name,self.image
  
class Author(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  
  def __str__(self):
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=100)
  authors = models.ManyToManyField(Author)
  publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE) # this topic fetch option from __str__ method of Topic class
    # since django 2.x on_delete is required with forein key
    
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
        """returns first 50 chars as string representaion of the data"""
        return self.text[:50]+"....."
    

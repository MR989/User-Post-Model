from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User1(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)    
    password=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    text=models.TextField()
    created_at=models.DateField()
    updated_at=models.DateField()

    def __str__(self):
        return self.text
    



from django.urls import reverse
from django.db import models
from datetime import datetime    

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # You can adjust the max_length as needed
   
    

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
    
        
    def __str__(self):
        return self.text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
  

class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    current_date = models.DateTimeField(default=datetime.now, blank=True)

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Post(models.Model):
    # this is a class to define posts for blog app 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title

































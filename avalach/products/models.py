from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Synopsis = models.TextField()
    Price = models.FloatField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
        
    

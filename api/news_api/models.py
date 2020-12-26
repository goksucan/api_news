from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

class News(models.Model):
    id_product = models.IntegerField
    product_id = models.IntegerField(max_length=10)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    resource = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    

from django.db import models

# Create your models here.
class Library1(models.Model):
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    pages = models.IntegerField()
    publication = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=100)

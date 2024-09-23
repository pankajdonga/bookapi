from django.db import models

# Create your models here.

class bookData(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    isbn=models.BigIntegerField()
    publisher=models.CharField(max_length=200)


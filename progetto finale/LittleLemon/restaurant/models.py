from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

class MenuItem(models.Model):
    title = models.SlugField()
    price = models.CharField(max_length=255)
    inventory = models.SmallIntegerField(max_digits =  6, decimal_places = 2)
    category= models.ForeignKey(Category, on_delete= models.PROTECT(),default=1)
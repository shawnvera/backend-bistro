from django.db import models

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=40)


class Cuisine(models.Model):
    type = models.CharField(max_length=40)

class menu_items(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    spicy_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
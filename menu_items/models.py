from django.db import models

# Create your models here.

class category(models.Model):
    type = models.CharField(max_length=40)
    # category = models.IntegerField()


class cuisine(models.Model):
    type = models.CharField(max_length=40)
    # cuisine = models.IntegerField()

class menu_items(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    spicy_level = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(cuisine, on_delete=models.CASCADE)
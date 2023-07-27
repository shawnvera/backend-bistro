from django.db import models

# Create your models here.

class category(models.Model):
    appetizer = models.CharField(max_length=40)
    dessert = models.CharField(max_length=40)
    main_dish = models.CharField(max_length=40)


class cuisine(models.Model):
    american = models.CharField(max_length=40)
    asian = models.CharField(max_length=40)
    mexican = models.CharField(max_length=40) 


class menu_items(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    spicy_level = models.IntegerField()
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey(cuisine, on_delete=models.CASCADE)
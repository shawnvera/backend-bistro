from django.db import models

# Create your models here.
class menu_items(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    spicy_level = models.IntegerField()
    category_id = models.IntegerField()
    cuisine_id = models.IntegerField()


class category(models.Model):
    appetizer = models.CharField(max_length=40)
    dessert = models.CharField(max_length=40)
    main_dish = models.CharField(max_length=40)
    id = models.ForeignKey(menu_items, on_delete=models.CASCADE)


class cuisine(models.Model):
    id = models.ForeignKey(menu_items, on_delete=models.CASCADE)
    american = models.CharField(max_length=40)
    asian = models.CharField(max_length=40)
    mexican = models.CharField(max_length=40) 
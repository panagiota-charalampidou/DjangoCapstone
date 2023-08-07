from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient = models.CharField()
    available_quantity = models.FloatField()
    measurement_unit = models.CharField()
    price_per_unit = models.FloatField()

class MenuItem(models.Model):
    menu_item = models.CharField()
    price = models.FloatField()

class RecipeRequirements(models.Model):
    menu_item = models.CharField()
    ingredient = models.CharField()
    ingredient_quantity = models.FloatField()
    measurement_unit = models.CharField()
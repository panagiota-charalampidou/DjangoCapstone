from django.db import models
import datetime

# Create your models here.
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=40)
    available_quantity = models.FloatField()
    measurement_unit = models.CharField(max_length=40)
    price_per_unit = models.FloatField()

    class Meta:
        ordering = ["ingredient"]
    
    def __str__(self):
        return self.ingredient

class RecipeRequirements(models.Model):
    menu_item = models.CharField(max_length=40)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_quantity = models.FloatField()

    class Meta:
        ordering = ["menu_item"]

    def __str__(self):
        return self.menu_item

class MenuItem(models.Model):
    menu_item = models.ForeignKey(RecipeRequirements, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        ordering = ["menu_item"]

    def __str__(self):
        return self.menu_item

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(default = datetime.date.today)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return self.menu_item
     

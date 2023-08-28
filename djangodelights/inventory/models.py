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
        return f"""
        name = {self.ingredient};
        available quantity = {self.available_quantity};
        unit = {self.measurement_unit};
        unit price = {self.price_per_unit}
        """
    
class MenuItem(models.Model):
    menu_item = models.CharField(max_length=40)
    price = models.FloatField()

    class Meta:
        ordering = ["menu_item"]

    def __str__(self):
        return f"{self.menu_item}; price={self.price}"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirements_set.all())
    

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_quantity = models.FloatField()

    class Meta:
        ordering = ["menu_item"]

    def __str__(self):
        return f"""
        Menu Item = {self.menu_item};
        Ingredient = {self.ingredient};
        Quantity = {self.ingredient_quantity}
        """
    
    def enough(self):
        return self.ingredient_quantity <= self.ingredient.available_quantity
    
    def cost_of_recipe(self):
        return self.ingredient_quantity * self.ingredient.price_per_unit


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(default = datetime.date.today)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"""
        Menu Item = {self.menu_item};
        Time = {self.timestamp};
        """
    
    def total_revenue(self):
        return self.menu_item.price()
    
     

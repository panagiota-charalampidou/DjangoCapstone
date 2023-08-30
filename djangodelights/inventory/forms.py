from django import forms
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase

class IngredientAddForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("ingredient", "available_quantity", "measurement_unit", "price_per_unit")

class MenuItemAddForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ("menu_item", "price")

class RecipeRequirementsAddForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = ("menu_item", "ingredient", "ingredient_quantity")


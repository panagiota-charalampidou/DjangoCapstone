from django import forms
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase

class IngredientAddForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("ingredient", "available_quantity", "measurement_unit", "price_per_unit")
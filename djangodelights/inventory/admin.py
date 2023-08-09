from django.contrib import admin
from .models import Ingredient, RecipeRequirements, MenuItem, Purchase

# Register your models here.
admin.site.register([Ingredient, RecipeRequirements, MenuItem, Purchase])
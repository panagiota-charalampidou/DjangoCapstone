from django.shortcuts import render
from .models import Ingredient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
   return render(request, 'inventory/home.html')

class IngredientList(ListView):
   model=Ingredient
   template_name="inventory/ingredients.html"
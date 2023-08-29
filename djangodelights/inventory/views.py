from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient, MenuItem, Purchase, RecipeRequirements
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientAddForm, MenuItemAddForm, RecipeRequirementsAddForm

# Create your views here.
def home(request):
   return render(request, 'inventory/home.html')

class IngredientList(ListView):
   model=Ingredient
   template_name="inventory/ingredients.html"

class IngredientDelete(DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"
  success_url = "/ingredients/list"

class IngredientAdd(CreateView):
   model = Ingredient
   template_name = "inventory/ingredient_add_form.html"
   form_class = IngredientAddForm


class MenuList(ListView):
   model = MenuItem
   template_name = "inventory/menu.html"


class MenuItemAdd(CreateView):
   model = MenuItem
   template_name = "inventory/menu_add_form.html"
   form_class = MenuItemAddForm

class RecipeRequirementsAdd(CreateView):
   model = RecipeRequirements
   template_name = "inventory/reciperequirements_add_form.html"
   form_class = RecipeRequirementsAddForm

class PurchaseList(ListView):
   model = Purchase
   template_name = "inventory/purchases.html"

class RevenueList(LoginRequiredMixin, TemplateView):
   model = Purchase
   template_name = "inventory/profit_revenue.html"

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirements_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * \
                    recipe_requirement.ingredient_quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context
   

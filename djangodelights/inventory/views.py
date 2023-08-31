from typing import Any, Dict
from django.shortcuts import redirect
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Ingredient, MenuItem, Purchase, RecipeRequirements
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientAddForm, MenuItemAddForm, RecipeRequirementsAddForm, PurchaseAddForm

# Create your views here.
class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name="registration/signup.html"

def logout_view(request):
   if request.method=="POST":
        logout(request)
        return redirect('login')

@login_required
def home(request):
   return render(request, 'inventory/home.html')

class IngredientList(LoginRequiredMixin, ListView):
   model=Ingredient
   template_name="inventory/ingredients.html"

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"
  success_url = "/ingredients/list"

class IngredientAdd(LoginRequiredMixin, CreateView):
   model = Ingredient
   template_name = "inventory/ingredient_add_form.html"
   form_class = IngredientAddForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
   model = Ingredient
   template_name = "inventory/ingredient_update_form.html"
   fields = ("ingredient", "available_quantity", "measurement_unit", "price_per_unit")
   success_url = "/ingredients/list"


class MenuList(LoginRequiredMixin, ListView):
   model = MenuItem
   template_name = "inventory/menu.html"

class MenuItemAdd(LoginRequiredMixin, CreateView):
   model = MenuItem
   template_name = "inventory/menu_add_form.html"
   form_class = MenuItemAddForm

class RecipeRequirementsAdd(LoginRequiredMixin, CreateView):
   model = RecipeRequirements
   template_name = "inventory/reciperequirements_add_form.html"
   form_class = RecipeRequirementsAddForm

class PurchaseList(LoginRequiredMixin, ListView):
   model = Purchase
   template_name = "inventory/purchases.html"

class PurchaseAdd(LoginRequiredMixin, CreateView):
   model = Purchase
   template_name = "inventory/purchase_add_form.html"
   form_class = PurchaseAddForm

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
      return context
   
   def post(self, request):
      menu_item_id = request.POST["menu_item"]
      menu_item = MenuItem.objects.get(pk=menu_item_id)
      requirements = menu_item.reciperequirements_set
      purchase = Purchase(menu_item=menu_item)

      for requirement in requirements.all():
         required_ingredient = requirement.ingredient
         required_ingredient.ingredient_quantity -= requirement.igredient_quantity
         required_ingredient.save()
      
      purchase.save()
      return redirect("/purchases")

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
   

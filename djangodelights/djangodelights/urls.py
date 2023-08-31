"""djangodelights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("django.contrib.auth.urls"), name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("", views.home, name="home"),
    path("ingredients/list", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("menu/list", views.MenuList.as_view(), name="menulist"),
    path("purchases", views.PurchaseList.as_view(), name="purchaselist"),
    path("profit_revenue", views.RevenueList.as_view(), name="profitrevenuelist"),
    path("ingredients/add", views.IngredientAdd.as_view(), name="ingredientadd"),
    path("menu/add", views.MenuItemAdd.as_view(), name="menuitemadd"),
    path("menu/add_recipe_requirement", views.RecipeRequirementsAdd.as_view(), name="reciperequirementadd"),
    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("purchases/add", views.PurchaseAdd.as_view(), name="purchaseadd")
]

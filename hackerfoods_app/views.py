from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {})

def detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {"recipe": recipe}
    return render(request, "recipe.html", context)

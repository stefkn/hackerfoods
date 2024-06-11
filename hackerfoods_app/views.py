from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    if request.htmx:
        template_name = "home.html"
    else: 
        template_name = "full/home_full.html"
    
    return render(request, template_name, context)

def about(request):
    if request.htmx:
        template_name = "about.html"
    else: 
        template_name = "full/about_full.html"

    return render(request, template_name, {})

def detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {"recipe": recipe}

    if request.htmx:
        template_name = "recipe_detail.html"
    else: 
        template_name = "full/recipe_detail_full.html"

    return render(request, template_name, context)

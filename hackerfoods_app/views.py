from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.db.models import Count, Sum
from .models import Recipe, Vote


def return_partial_or_full(request, partial_template, full_template):
    if request.htmx:
        template_name = partial_template
    else:
        template_name = full_template

    return template_name


def recipes(request):
    recipes = Recipe.objects.all().annotate(
        vote_sum=Sum("vote__vote_value")
    )
    context = {"recipes": recipes}

    template_name = return_partial_or_full(
        request, "recipes.html", "full/recipes_full.html"
    )

    return render(request, template_name, context)


def about(request):
    template_name = return_partial_or_full(
        request, "about.html", "full/about_full.html"
    )

    return render(request, template_name, {})

class AboutView(TemplateView):
    template_name = "about.html"


def detail(request, recipe_id):
    context = {"recipe": get_object_or_404(Recipe, pk=recipe_id)}
    template_name = return_partial_or_full(
        request, "recipe_detail.html", "full/recipe_detail_full.html"
    )

    return render(request, template_name, context)


def vote(request, recipe_id, vote_value):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    vote = Vote.objects.create(recipe=recipe, vote_value=vote_value)
    vote.save()

    return render(request, "vote.html", {"recipe": recipe, "vote": vote})


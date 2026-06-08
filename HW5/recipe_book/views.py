from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipe_book/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_book/recipe_detail.html', {'recipe': recipe})


def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        Recipe.objects.create(
            name=name,
            description=description,
            ingredients=ingredients,
            instructions=instructions
        )
        Recipe.export_to_json()
        return redirect('recipe_list')

    return render(request, 'recipe_book/add_recipe.html')


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.description = request.POST.get('description')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.instructions = request.POST.get('instructions')
        recipe.save()
        Recipe.export_to_json()
        return redirect('recipe_detail', recipe_id=recipe.id)

    return render(request, 'recipe_book/edit_recipe.html', {'recipe': recipe})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    Recipe.export_to_json()
    return redirect('recipe_list')

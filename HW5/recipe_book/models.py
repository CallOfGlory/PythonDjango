from django.db import models
import json
from pathlib import Path


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def export_to_json(cls):
        recipes = cls.objects.all()
        data = []
        for recipe in recipes:
            data.append({
                'id': recipe.id,
                'name': recipe.name,
                'description': recipe.description,
                'ingredients': recipe.ingredients,
                'instructions': recipe.instructions,
            })

        file_path = Path(__file__).resolve().parent / 'recipes.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def import_from_json(cls):
        file_path = Path(__file__).resolve().parent / 'recipes.json'
        if not file_path.exists():
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            cls.objects.update_or_create(
                id=item['id'],
                defaults={
                    'name': item['name'],
                    'description': item['description'],
                    'ingredients': item['ingredients'],
                    'instructions': item['instructions'],
                }
            )

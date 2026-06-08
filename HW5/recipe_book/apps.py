from django.apps import AppConfig


class RecipeBookConfig(AppConfig):
    name = 'recipe_book'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from .models import Recipe
        Recipe.import_from_json()

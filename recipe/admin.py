from django.contrib import admin
from .models import Recipe, RecipeText, Ingredient, Contact

admin.site.register([Recipe, RecipeText, Ingredient, Contact])

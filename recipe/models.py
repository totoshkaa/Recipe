from typing import Any
from django.db import models
from django.utils import timezone
from users.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    image = models.ImageField(upload_to="recipes-images/")
    created_at = models.DateTimeField(auto_now_add=True)
    prep = models.IntegerField()
    cook = models.IntegerField()
    
    def __str__(self):
       return self.name

    def __str__(self) -> str:
        return f'text -> {self.name} star -> {self.star}'

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

def __str__ (self) -> str:
    return self.name


class Comment(models.Model):
    recipe = models.ForeignKey('Recipe', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.recipe}'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
    
class CommentRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    rating = models.IntegerField(default=1)  # Rating field,  to 1 star

    def __str__(self) -> str:
        return self.text[:50]
    
    
class RecipeText(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    text = models.TextField()



class MainPage(models.Model):
    pass
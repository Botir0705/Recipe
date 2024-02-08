from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    ingredients = models.TextField(blank=True)
    content = models.TextField(default = '')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    

class ProfileRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
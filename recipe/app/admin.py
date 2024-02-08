from django.contrib import admin
from .models import Recipe, ProfileRecipe


admin.site.register(Recipe)
admin.site.register(ProfileRecipe)
from django.urls import path
from . import views


urlpatterns = [
    path('', views.log_in, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.log_out, name='logout'),
    path('main/', views.main, name='main'),
    path('main/<str:title>', views.recipe_detail, name='recipe_detail'),
    path('main/<str:title>/add', views.add_recipe, name='add'),
    path('main/<str:title>/remove', views.remove_recipe, name='remove'),  
    path('profile', views.profile_recipes, name='profile')
]

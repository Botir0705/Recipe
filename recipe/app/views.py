from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginUserForm
from .models import Recipe, ProfileRecipe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


my_recipes = set()

@login_required(login_url='login')
def main(request):
    search_query = request.GET.get('search', '')
    recipes = Recipe.objects.all().order_by('-created_on')

    if  search_query:
        recipes = recipes.filter(title__icontains=search_query)
    else:
        pass

    return render(request, 'app/main.html', {'recipes': recipes, 'search_query': search_query})


@login_required(login_url='login')
def recipe_detail(request, title):
    recipe = Recipe.objects.get(title=title)
    return render(request, 'app/detail.html', {'recipe': recipe})


@login_required(login_url='login')
def add_recipe(request, title):
    recipe = Recipe.objects.get(title=title)
    my_recipes.add(recipe)
    return redirect('profile')


@login_required(login_url='login')
def remove_recipe(request, title):
    recipe = Recipe.objects.get(title=title)
    my_recipes.remove(recipe)
    return redirect('profile')


login_required(login_url='login')
def profile_recipes(request):
    recipes = my_recipes
    return render(request, 'app/profile.html', {'recipes': my_recipes})


def sign_up(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'app/sign_up.html', {'form': form})


def log_in(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            
    return render(request, 'app/login.html', {'form': form})


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('login')


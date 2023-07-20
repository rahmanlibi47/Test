from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SuperHeroes
from .forms import HeroForms


def entepage(request):
    return render(request, 'home.html')

def park(request):
    return render(request, 'park.html')

def theatre(request):
    return render(request, 'theatre.html')

@login_required
def display_superheroes(request):
    heroes = SuperHeroes.objects.all()
    return render(request, 'heroes.html', {'heroes' : heroes})

@login_required
def add_superhero(request):
    if request.method == 'POST':
        form = HeroForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_hero')
    else:
        form = HeroForms()
    return render(request, 'add_hero.html', {'form' : form})

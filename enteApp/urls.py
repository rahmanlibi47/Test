from django.urls import path
from .views import entepage, theatre, park, display_superheroes, add_superhero

urlpatterns = [
    path('', entepage, name='home'),
    path('park/', park),
    path('theatre/', theatre),
    path('heroes/', display_superheroes, name='display_hero'),
    path('heroes/add', add_superhero, name='add_hero'),
    

]
from django import forms
from .models import SuperHeroes

class HeroForms(forms.ModelForm):
    class Meta:
        model = SuperHeroes
        fields = ['name', 'power', 'universe']
        

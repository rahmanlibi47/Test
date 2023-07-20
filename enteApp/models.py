from django.db import models


class SuperHeroes(models.Model):
    name = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    universe = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

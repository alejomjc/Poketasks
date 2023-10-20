from django.contrib.auth.models import User
from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', blank=False, null=False)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', blank=False, null=False)
    ability = models.ManyToManyField(Ability, verbose_name='Abilities', blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation Date', null=True, blank=True)
    api_creation = models.BooleanField(verbose_name='Api Creation', blank=True, null=True)

    def __str__(self):
        return '{0} -> {1}'.format(self.name, ', '.join(self.ability.values_list('name', flat=True)))

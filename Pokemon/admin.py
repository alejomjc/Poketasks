from django.contrib import admin

from Pokemon.models import Pokemon, Ability


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creation_date', 'api_creation')
    list_display_links = ('id', 'name', 'creation_date', 'api_creation')
    search_fields = ('id', 'name', 'creation_date', 'api_creation')


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

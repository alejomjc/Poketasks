# Generated by Django 4.2.6 on 2023-10-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemon', '0004_rename_hability_ability_remove_pokemon_hability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='ability',
            field=models.ManyToManyField(blank=True, null=True, to='Pokemon.ability', verbose_name='Abilities'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemon', '0002_remove_pokemon_hability_pokemonhability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.DeleteModel(
            name='PokemonHability',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hability',
            field=models.ManyToManyField(blank=True, to='Pokemon.hability', verbose_name='Habilities'),
        ),
    ]

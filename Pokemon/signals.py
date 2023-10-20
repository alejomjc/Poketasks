from django.db.models.signals import post_save
from django.dispatch import receiver

from Poketasks.settings import DEFAULT_FROM_EMAIL
from .models import Pokemon
from django.core.mail import send_mail


@receiver(post_save, sender=Pokemon)
def send_pokemon_creation_notification(sender, instance, **kwargs):
    subject = 'Una Prueba real'
    message = f'Se ha creado el Pokémon: {instance.name}'
    recipient_list = ['alejomjc2011@gmail.com']
    send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)

import random
import logging
import time
from celery import shared_task
from Pokemon.models import Ability

logger = logging.getLogger(__name__)


@shared_task
def mi_tarea():
    time.sleep(5)
    logger.info('Asereje')
    Ability.objects.create(name='Habilidad{0}'.format(random.randint(1, 1000)))
    pass

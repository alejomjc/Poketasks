# Poketasks

Esta es una aplicación Django llamada "Poketasks" diseñada para gestionar información sobre Pokémon y realizar tareas automatizadas.

## Características

- Administración de los modelos desde el Admin de Django que permite a los usuarios listar, buscar y agregar habilidades.

- API REST que permite crear y buscar con documentación en Swagger.

- Autenticación implementada para garantizar la seguridad de los endpoints de la API.

- Uso de Celery para ejecutar una tarea que extrae un información aleatoria cada cierto tiempo desde un API externo, y luego lo envía a la API creada en la aplicación.

- Notificaciones por correo electrónico utilizando Django Signals.

- Registro de logs de los Pokémon repetidos.

## Configuración

Para comenzar a usar la aplicación, sigue estos pasos:

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/Poketasks.git
```
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Realiza las migraciones:
```bash
python manage.py migrate
```
4. Inicia el servidor:
```bash
python manage.py runserver
```
5. Accede a la aplicación en http://localhost:8000/.

## Ejecución de Tareas Celery
Para ejecutar las tareas Celery, asegúrate de tener un worker Celery en funcionamiento. Puedes iniciar el worker con el siguiente comando:
```bash
celery -A Poketasks worker -l info
```
Para ejecutar las tareas Celery programadas, asegúrate de tener un worker Celery en funcionamiento. Puedes iniciar el beat con el siguiente comando:
```bash
celery -A Poketasks beat -l info
```
## Ejecución de Pruebas Unitarias
Para ejecutar las pruebas unitarias, utiliza el siguiente comando:
```bash
python manage.py test
```
## Contribuciones
¡Contribuciones son bienvenidas! Si tienes sugerencias, problemas o mejoras, no dudes en abrir un issue o enviar un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.

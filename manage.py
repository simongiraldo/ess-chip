#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'essApp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#Ahora una pequena documentacion de como funciona el archivo manage.py
"""
Este archivo es el que se encarga de ejecutar las tareas administrativas de django, como por ejemplo:
    - Crear un proyecto
    - Crear una aplicacion
    - Migrar la base de datos
    - Correr el servidor de desarrollo
    - Correr los test
    - etc

Para ejecutar una tarea se debe ejecutar el siguiente comando:
    python manage.py <nombre de la tarea>
    
Ejemplo:
    python manage.py runserver
    python manage.py createsuperuser
    python manage.py startapp <nombre de la aplicacion>
    python manage.py makemigrations
    python manage.py migrate
    python manage.py test
    etc

Para ver todas las tareas que se pueden ejecutar con el comando manage.py se debe ejecutar el siguiente comando:
    python manage.py help
"""
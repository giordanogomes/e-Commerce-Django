"""
Configuração WSGI para o projeto pystore.

Ele expõe o WSGI callable como uma variável de nível de módulo chamada ``application``.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pystore.settings')

application = get_wsgi_application()

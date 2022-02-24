from django.apps import AppConfig

# Configuração do app Products
# Deve ser colocado dentro de INSTALLED_APP em settings.py
class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

"""Configuração de URL do pystore

A lista `urlpatterns` encaminha URLs para visualizações. Para mais informações consulte:
     https://docs.djangoproject.com/en/4.0/topics/http/urls/
Exemplos:
Visualizações de funções
     1. Adicione uma importação: das visualizações de importação my_app
     2. Adicione um URL a urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
     1. Adicione uma importação: from other_app.views import Home
     2. Adicione um URL a urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
     1. Importe a função include(): from django.urls import include, path
     2. Adicione um URL a urlpatterns: path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

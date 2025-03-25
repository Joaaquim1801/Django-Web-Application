"Todas as possíveis rotas da aplicação estão aqui"

"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

"Esse path vai indicar assim: Para rota X execute essa função"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

#MEDIA_URL = Define a URL base para acessar os arquivos de mídia
#MEDIA_ROOT = Define o DIRETÓRIO no sistema de arquivos onde os arquivos de mídia são armazenadas

from django.contrib import admin
from galeria.models import Fotografias

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id","nome")
    search_fields = ("nome","categoria") #Precisa ser uma tupla

admin.site.register(Fotografias, ListandoFotografias)

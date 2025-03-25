from django.contrib import admin
from galeria.models import Fotografias

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicado")
    list_display_links = ("id","nome")
    search_fields = ("nome",) #Precisa ser uma tupla
    list_filter = ("categoria",)
    list_per_page = 10
    list_editable = ("publicado",)


admin.site.register(Fotografias, ListandoFotografias)

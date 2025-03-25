from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias

def index(request):
    fotografias = Fotografias.objects.order_by("data_fotografia").filter(publicado=True) #O all() Vai acessar os objetos no banco de dados
    #já o filter vai filtrar aqueles que possuem a característica mencionada
    #order_by() ele vai ordenar os itens já cadatrados com base em uma informação
    #-data_fotografia = ordenar pelo mais antigo, o "-" tem a função de tipo fazer o inverso
    return render(request, 'galeria/index.html', {"cards": fotografias })

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk= foto_id) #Acessar o objeto no banco de dados ao qual o id faz referência
    #pk =  "Primary Key"
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})
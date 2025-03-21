from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias

def index(request):
    fotografias = Fotografias.objects.all() # Vai acessar os objetos no banco de dados
    return render(request, 'galeria/index.html', {"cards": fotografias })

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk= foto_id) #Acessar o objeto no banco de dados ao qual o id faz referência
    #pk =  "Primary Key"
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})
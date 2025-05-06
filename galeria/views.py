from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografias
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated: #Valida se o usuário está logado no site
        messages.error(request, "ERRO! O usuário não fez login")
        return redirect('login')
    
    fotografias = Fotografias.objects.order_by("data_fotografia").filter(publicado=True) #O all() Vai acessar os objetos no banco de dados
    #já o filter vai filtrar aqueles que possuem a característica mencionada
    #order_by() ele vai ordenar os itens já cadatrados com base em uma informação
    #-data_fotografia = ordenar pelo mais antigo, o "-" tem a função de tipo fazer o inverso
    return render(request, 'galeria/index.html', {"cards": fotografias })

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk= foto_id) #Acessar o objeto no banco de dados ao qual o id faz referência
    #pk =  "Primary Key"
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})

def buscar(request):

    if not request.user.is_authenticated:
        messages.error(request, "ERRO! O usuário não fez login")
        return redirect('login')

    fotografias = Fotografias.objects.order_by("data_fotografia").filter(publicado=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] #Ele pega o nome que o usuário digitou
        if nome_a_buscar:
            fotografias = Fotografias.objects.filter(nome__contains= nome_a_buscar) #nome__contains verifica se dentro de Fotografias tem um item que no nome dele tem o "nome_a_buscar" como se fosse um for

    return render(request, "galeria/buscar.html", {"cards": fotografias})
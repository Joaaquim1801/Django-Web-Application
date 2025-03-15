from django.shortcuts import render


def index(request):
    dados = {
    1:{'nome': 'Crab Nebula',
    'legenda': 'webbtelescope.org / NASA / James Webb'},
    2:{'nome': 'Arp 220 Galaxy',
    'legenda': 'webbtelescope.org / NASA / James Webb'}
    }
    return render(request, 'galeria/index.html', {"cards": dados })

def imagem(request):
    return render(request, 'galeria/imagem.html')
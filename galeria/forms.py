from django import forms
from galeria.models import Fotografias

class FotografiasForms(forms.ModelForm): #O Django tem uma ferramenta que cria um formulário a partir de um model, basta indicar qual model é
    class Meta: #metadados, ver sobre
        model = Fotografias
        exclude = ['publicado',]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                    }
                ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

#o'attrs=' é utilizado para adicionar atributos HTML ao campo do formulário
#o class FotografiaForms é uma forma do django organizar o que vai ser visto pelo usuário como formulário no HTML, já o class Meta, cuja funcionalidade é bem interessante,
#tem a missão de "dizer" como que essa classe maior vai se organizar, como ela vai se comportar, quais vão ser os dados que vão ser utilizados para a criação dos formulários
#dentro de Meta é relacionado o model que será utilizado para o formulário ser baseado
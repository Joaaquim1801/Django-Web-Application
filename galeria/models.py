from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#Aqui é onde fica a parte do banco de dados objeto-relacional

class Fotografias(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("NEBULOSA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA,default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User, #Associar a tabela de usuário do própio django; Acessa a tabela própia do Django de usuários
        on_delete= models.SET_NULL, #Caso um usuário que criou um um novo item for apagado 
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return self.nome
    
#makemigrations = cria um novo arquivo de migrations, cria um novo campo
#migrate = 
#A alteração feita foi o ImageField -> assim eu vou designar uma nova forma de fazer um CRUD
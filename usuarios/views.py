from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method ==  'POST':
        form = LoginForms(request.POST)

        if form.is_valid(): #--> se ele for válido, ou seja, se os campos obrigatórios foram preenchidos e a tipagem dos dados
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate( #Retorna None ou o objeto que representa o usuário ( banco de dados )
            #.authenticate -> É responsável por verificar as informações dadas pelo usuário na página de login existe dentro do banco de dados
            request, #-> Contém informações sobre o tipo de requisição HTTP que foi feita no site
            username=nome,
            password=senha
        #request, username, e password são parâmetros para o método authenticate()
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, "Login feito com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "ERRO! Ao efetuar o login")
            return redirect('login')
        
    return render(request, "usuarios/login.html", {"forms": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST) #Pega todas as informações do usuário e coloca dentro do formulário novo

        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha1'].value()

            if User.objects.filter(username=nome).exists(): #Se quando efetuar o cadastro o usuário já tiver sido cadastrado no banco de dados
                messages.error(request, "Usuário já existente!")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')
        
    return render(request, "usuarios/cadastro.html", {"forms": form})

def logout(request):
    if not request.user.is_authenticated:
        messages.error(request, "O usuário precisa fazer login antes de sair")
        return redirect('login')
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')
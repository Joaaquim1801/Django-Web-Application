from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: José da Silva"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={ #Atributos
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: José da Silva"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget= forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: josesilva@hotmail.com"
            }
        )
    )
    senha1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha2 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")  #Por que usar self.cleaned_data? Pois se eu usasse apenas self.nome_cadastro a variável poderia estar com dados não validados e
        #limpos, ou seja, poderia dar um erro depois caso não usasse isso
        #O .get vai servir para pegar essa chave do dicionário, caso ela não existe retornará None, evitando erros, como o KeyError
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError("Não é permitido colocar espaços dentro do campo")
            else:
                return nome       
    def clean_senha2(self): #É importante que nome da função seja: clean_nomedavariavel, esse nomedavariavel tem que ser exatamente o que está dentro da classe
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("As senhas não são iguais!")
            else:
                return senha2

    
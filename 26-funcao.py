import os

os.system("cls")  # limpar tela (Windows)

# criando a primeira função
def escreva():
    print("Olá mundo")

# chamando a função
escreva()

# função com parâmetros
def exibir_dados(nome, idade, email):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")
    print("=" * 100)

# chamando a função novamente
escreva()

# exibindo dados
exibir_dados("Caio", 38, "caio@email.com")

# função com retorno
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

# chamando a função com retorno
total = somar(10, 20)
print(f"Total: {somar(10,20)}")




   
   
   
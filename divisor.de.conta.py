import os
os.system("cls")

def calcular_parte(valor_conta, numero_pessoas):
    valor_por_pessoa = valor_conta / numero_pessoas
    return valor_por_pessoa

print("Bem-vindo ao calculador de divisão de contas")
valor_conta = float(input("Digite o valor total da conta: R$"))
numero_pessoas = int(input("Informe quantas pessoas vão dividir: "))

valor_por_pessoa = calcular_parte(valor_conta, numero_pessoas)

print(f"Valor total da conta: R${valor_conta}")
print(f"Número de pessoas: {numero_pessoas}")
print(f"Cada pessoa deve pagar: R${valor_por_pessoa}")
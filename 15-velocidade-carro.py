import os
os.system("cls")
velocidade = float(input("Digite a velocidade do veículo: "))

if velocidade > 80:
    print("Você recebeu uma multa!!!")
else:
    print("você está dentro do limite de velocidade")
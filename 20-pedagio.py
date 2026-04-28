import os
os.system("cls")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")

tipo = int(input("Digite o tipo de veículo: "))

if tipo == 1:
    print("Valor do pedágio: R$10")
elif tipo == 2:
    print("Valor do pedágio: R$5")
elif tipo == 3:
    print("Valor do pedágio: R$20")
else:
    print("Veiculo inválido")
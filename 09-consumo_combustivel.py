import os
os.system("cls")
km = float(input("Digite os quilômetros percorridos: "))
litros = float(input("Digite a quantidade de litros gastos: "))

consumo = km / litros
print(f"Consumo médio: {consumo:.2f} km/l")
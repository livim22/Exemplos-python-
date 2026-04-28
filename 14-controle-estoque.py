import os
os.system("cls")
quantidade = int(input("Digite a quantidade em estoque: "))

if quantidade < 5:
    print("Estoque baixo, favor repor!")
else:
    print("Estoque aceitavel!")
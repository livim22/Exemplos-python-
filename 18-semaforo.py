import os
os.system("cls")
cor = input("Digite a cor do semáforo: ").lower()

if cor == "verde":
    print("Pode atravessar")
elif cor == "amarelo":
    print("preste atenção")
elif cor == "vermelho":
    print("Pare!!")
else:
    print("Cor inválida")
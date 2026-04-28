import os
os.system("cls")
import random

numero = random.randint(1, 10)
palpite = int(input("Adivinhe o número (1 a 10): "))

if palpite == numero:
    print("Acertou, uhullll!")
else:
    print(f"Errou!!! O número era {numero} que pena!")
import os
os.system("cls")
horas = float(input("Quantas horas por dia você estuda? "))

if horas < 2:
    print("Você possui pouco estudo!")
elif horas <= 4:
    print("Você possui um estudo moderado!")
else:
    print("Você tem estudado muito!")
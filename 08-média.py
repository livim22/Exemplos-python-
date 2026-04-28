import os
from statistics import median

os.system("cls")
print("seja bem vindo ao boletim escolar!")

nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
nota3=float(input("digite a terceira nota:"))
total=(nota1+nota2+nota3) /3
print("sua média é:",total)

if (median>=7):
     
     print("você foi aprovado!")
elif(median>=4 and median<=6):
     
     print("você está de recuperação!")
else:
     print("você reprovou!")

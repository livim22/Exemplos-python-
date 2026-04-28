import os
os.system("cls")

numero1=float(input("Digite um número:"))
numero2=float(input("Digite outro númro:"))
operacao= input("escolha a operação desejada")

if(operacao == "+"):
    resultado=numero1+numero2

elif(operacao== "-"):
    resultado=numero1-numero2 


elif(operacao == "*"):

    resultado=numero1*numero2


elif (operacao == "/"):

    resultado=numero1/numero2

else: 
    print("opção inválida")  


print("o resultado é:", resultado)


print("Espero ter ajudado!")
input("pressione <enter> para encerrar")
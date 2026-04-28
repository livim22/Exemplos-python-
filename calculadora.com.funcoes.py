import os 
os.system("cls")

print("seja bem vindo a super calculadora 2.0 pro max!")

numero1=int(input("informe o primeiro número:"))
numero2=int(input("informe o segundo número:"))

def somar(numero1, numero2):
   resultado= numero1+numero2
   return = resultado

def subtrair(numero1,numero2):
   resultado=numero1 - numero2
   return resultado

def multiplicar(numero1,numero2):
   resultado=numero1 * numero2
   return resultado

def dividir(numero1,numero2):
   resultado=numero1 : numero2
   return resultado


print("escolha uma das opções abaixo:")
print("[1]-somar")
print("[2]-subtrair")
print("[3]-multiplicar")
print("[4]-dividir")

if(opcao == 1):
   print(f"a soma é:{somar(numero1,numero2)}")

elif(opcao == 2):
   print(f"a subtração é:{subtrair(numero1,numero2)}")

elif(opcao == 3):
   print(f"a multiplicação é:{multiplicar(numero1,numero2)}")

elif(opcao == 4):
   print(f"a divisão é:{dividir(numero1,numero2)}")


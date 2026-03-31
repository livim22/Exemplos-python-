import os
os.system("cls)")
vida_jogador = 100
vida_inimigo = 100
while vida_jogador >= 0 and vida_inimigo >= 0: 


    jogando = True

while jogando == True:
    print("Bem-vindo ao jogo de batalha!")
    print("1. Atacar")
    print("2. curar")
    print("3. Fugir")
    escolha = input("Escolha sua ação: ")

    if escolha == "1":
        print("Você atacou o inimigo!")
        vida_inimigo -=10
    elif escolha == "2":
        print("Você se curou!")
        vida_jogador += 5
    elif escolha == "3":
        print("Você fugiu do combate!")
        jogando = False
    else:
        print("Tente novamente!")
    if vida_inimigo <= 0:
        print("Parabéns! Você venceu a batalha!")
        jogando = False
    elif vida_jogador <= 0:
        print("Você foi derrotado! Tente novamente.")
        jogando = False

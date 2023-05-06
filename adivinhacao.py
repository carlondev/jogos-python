import random


def jogar():

    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!!!")
    print("***********************************")


    # Variáveis do jogo
    numero_secreto   = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000


    # Nível de jogo
    print("Qual nível de dificuldade você escolhe?")
    print("[1] Fácil = 7 tentativas    [2] Médio = 5 tentativas   [3] Díficil = 3 tentativas")  

    nivel = int(input("Defina o nível de jogo: "))

    if(nivel == 1):
        total_tentativas = 7
    elif(nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3
        

    # Tentativas
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_tentativas))
        chute       = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute)
        numero_user = int(chute)
        
        if(numero_user < 1 or numero_user > 100):
            print("Você deve digitar um número entre 1 e 100!! Tente novamente:")
            continue

        acertou     = numero_user == numero_secreto
        chute_maior = numero_user > numero_secreto
        chute_menor = numero_user < numero_secreto
        

    # Resultados e pontuação
        if(acertou):
            print("VOCÊ ACERTOU!!! :)")
            print("Sua pontuação foi: ", pontos)
            break   
        else:
            if(chute_maior):
                print("Seu chute foi maior do que o número correto!")
            elif(chute_menor):
                print("Seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - numero_user)
            pontos = pontos - pontos_perdidos
            

    print("O número secreto é: ", numero_secreto)
    print("Sua pontuação foi {} de 1000 pontos.". format(pontos))
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()

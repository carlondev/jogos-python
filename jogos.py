import forca
import adivinhacao

def escolhe_jogo():
    print("**********************************")
    print(":::::::ESCOLHA O SEU JOGO!::::::::")
    print("**********************************")

    print ("[1] Forca   [2] Advinhação")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("JOGO DA FORCA")
        forca.jogar()
    elif(jogo == 2):
        print("JOGO DA ADIVINHAÇÃO")
        adivinhacao.jogar()
        
if(__name__ == "__main__"):
    escolhe_jogo()
import forca
import adivinhacao

def which_game():
    print("*********************************")
    print("*****Escolha o Jogo Desejado*****")
    print("*********************************")
    print()
    print("[1] - Forca")
    print("[2] - Adivinhação")


    game = int(input("Qual jogo? "))

    if game == 1:
        print("Jogando Forca")
        forca.play()
    elif game == 2:
        print("Jogando adivinha")
        adivinhacao.play()


if __name__ == "__main__":
    which_game()


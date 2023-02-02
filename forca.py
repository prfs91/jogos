
def jogar():
    print("*********************************")
    print("** Bem-vindo no jogo de Forca! **")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (True):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo.")

if (__name__ == "__main__"):
    jogar()
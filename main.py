import random

def adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            tentativa = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Isso não é um número válido. Tente novamente.")
            continue

        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    adivinhacao()

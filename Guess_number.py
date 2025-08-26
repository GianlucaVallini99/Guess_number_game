import random


def crea_numero():
    numero = random.randint(1, 100)
    return numero

def difficolta():
    while True:
        print("Scegli la difficoltà: ")
        Choice = input("FACILE o DIFFICILE? ")
        if Choice.upper() == "FACILE":
            tentativi = 10
            break
        elif Choice.upper() == "DIFFICILE":
            tentativi = 5
            break
        else:
            print("Scelta non valida ")
    return tentativi

def confronta(numero, vite):
    i = 0
    while vite > 0:
        guess = int(input("Inserisci il numero: "))
        if guess == numero:
            print(f"Complimenti! Hai indovinato il numero in {i} tentativi!")
            break
        elif guess > numero:
            vite -= 1
            i += 1
            print("Accidenti, hai inserito un numero troppo alto! ")
            if vite != 0:
                print(f"Ti rimangono solamente {vite} tentativi!")
        else:
            vite -= 1
            i += 1
            print("Accidenti, hai inserito un numero troppo basso! ")
            if vite != 0:
                print(f"Ti rimangono solamente {vite} tentativi!")

    return()

def main():
    while True:
        numero = crea_numero()
        tentativi = difficolta()
        confronta(numero, tentativi)

        play = input("Vuoi giocare ancora? Schiaccia 'SI' in caso affermativo, qualsiasi altra cosa altrimenti: ")
        if play != "SI":
            print("Grazie per aver giocato con noi! ")
            break

if __name__ == "__main__":
    main()


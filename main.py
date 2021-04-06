import random


with open("slowa.txt", "r") as file:
    lines = file.read().splitlines()


# variables
password = random.choice(lines)
password_letters = []
chances = 9
game = True


# dodawnanie liter do tablicy hasla
for el in password:
    password_letters.append(el)


def menu():
    print("1.Rozpocznij gre")
    print("2.Wyjsc z gry")


def password_display():
    global game
    global chances
    global password
    global password_letters
    guessed_letters = []
    
    for el in range(chances):
        for letter in range(len(password)):
                print("_", end=" ")
        print()
        choice = input("Letter:").lower()
        if len(choice) == 1: # dlugosc wpisanej litery nie moze byc wieksza niz 1
            if choice not in guessed_letters: # nie mozna zgadywac dwa razy tej samej litery
                guessed_letters.append(choice)
                if choice in password:
                    print(f"Odgadnieto literke {choice}!")
                    password_letters.remove(choice)
                    if not password_letters:
                        print("Odgadles haslo!")
                        game = False
                        break

                else:
                    print("Nie odgadnieto")
                    chances -= 1
                    if chances == 0:
                        game = False
            else:
                print("Ta literke juz podales!")
        else:
            print("Wpisz tylko jedna litere!")


def main():
    global game
    while game:
        menu()
        choice = input("Wybor:")
        if choice == '1':
            password_display()
        if choice == '2':
            game = False
            print("Do zobaczenia!")
        else:
            print("Zly wybor")
            print('\n' * 10)


main()

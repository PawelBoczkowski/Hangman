import random


with open("slowa.txt", "r") as file:
    lines = file.read().splitlines()


# variables
password = random.choice(lines)
password_letters = []
chances = 9
game = True


# Adding letter to the password table
for el in password:
    password_letters.append(el)


def menu():
    print("1.Start game")
    print("2.Exit")


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
        if len(choice) == 1: # lenght of word cannot be less than one
            if choice not in guessed_letters: # you cannot guess the same letter twice
                guessed_letters.append(choice)
                if choice in password:
                    print(f"You guessed letter {choice}!")
                    password_letters.remove(choice)
                    if not password_letters:
                        print("You guessed password!")
                        game = False
                        break

                else:
                    print("Don't guessed")
                    chances -= 1
                    if chances == 0:
                        game = False
            else:
                print("You have already given this letter!")
        else:
            print("Please enter only one letter!")


def main():
    global game
    while game:
        menu()
        choice = input("Choice:")
        if choice == '1':
            password_display()
        if choice == '2':
            game = False
            print("See you!")
        else:
            print("Wrong choice")
            print('\n' * 10)


main()

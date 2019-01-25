from Quiz import Quiz
from sys import exit
Game = Quiz(int(input("How many players?: ")))


def Menu():
    Choice = input("New Question(1), End Game(2): ")
    return Choice


try:
    while 1:
        choice = Menu()
        if choice == '1':
            Game.WhoAnswers()
        elif choice == '2':
            Game.PrintGameStatus()
            break
        else:
            print("Wrong choice...")
            continue
except KeyboardInterrupt:
    exit(0)

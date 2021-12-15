#Random Number Game
from random import randint
n = 0
random_num = randint(1,10)
player_input = input("Guess a number between 1 and 10:  ")

while n < 2:
    if player_input == random_num & n < 2:
        print("Congrats you guessed right! The answer was: ", player_input)
    elif player_input != random_num & n < 2:
        player_guess = input("Try again: ")
    else:
        print("nice try! The correct answer was: ", random_num, " Play again?")
    n = n + 1







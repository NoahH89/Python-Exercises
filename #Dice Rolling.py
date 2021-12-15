#Dice Rolling
from random import randint

the_dice = randint(1,6)
dice_roller = input("Say 'roll' whenever you're ready! ")

if dice_roller == "roll":
    print("You rolled a: ", the_dice)
    dice_roller = input("Would you like to roll again? ")
    if dice_roller == "yes":
        new_dice = randint(1,6)
        print("This time you rolled a: ", new_dice)
    elif dice_roller == "no":
        print("thank you for playing!")
elif dice_roller == "no" or dice_roller == "no thank you":
    print("Maybe next time then.")
else:
    print("Whatever you say weirdo..")

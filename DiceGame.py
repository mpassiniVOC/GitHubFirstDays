import random

def diceRoll():
    diceValue = random.randint(1,6)
    return diceValue

def startGame():
    print("Welcome to Dice Game! Its your roll vs. theirs!")
    ourRoll = diceRoll()
    theirRoll = diceRoll()
    print("You rolled a " + str(ourRoll))
    print("Your opponent rolled a " + str(theirRoll))
    if ourRoll == theirRoll:
        print("tie")
    elif ourRoll > theirRoll:
        print("You win!")
    else:
        print("You lose!")

startGame()



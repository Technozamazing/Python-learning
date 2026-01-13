# This is a simple random number gussing game to demonstrate the use of random module.

import random

ranNum = random.randint(1,10)

print(f'\n------------ Instruction ------------\n1. This is a random number Gussing Game.\n2. You have to guess a number btn 1 to 10.\n3. The program would have already gussed a random number.\n4. If your guess matches the system guess, You are the Winner\n5. But do remeber that you will only have 5 life time to guess. Exceding limit means failing.\n')
life = 5

while life > 0:
    guess = int(input("\nEnter a random number from (1 to 10): "))
    if guess == ranNum:
        print(f'Your Guess {guess} was right.\nYou made it at {life} attempt!\n')
    else:
        print(f"Your Guess wasn't right!\nBetter luck next time.\n") 
    life -= 1

if life == 0:
    print("5 life time is Used!\nBetter luck next time.\nThe correct number was {ranNum}\n")
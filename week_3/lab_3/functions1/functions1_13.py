import random

num = random.randint(1, 20)
name = input("Hello! What is your name? \n")

guess = int(input(f'Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess\n'))
count = 0
while guess != num:
    count += 1
    if guess < num:
        guess = int(input("Your guess is too low. \nTake a guess\n"))
    else:
        guess = int(input("Your guess is too high. \nTake a guess\n"))
    

    
else:
    print(f"Good job, {name}! You guessed my number in {count} guesses!")


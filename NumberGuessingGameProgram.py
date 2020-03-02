#This program allows the user to enter a number while the program tries to guess the number


import random
n=random.randint(1,100)
guess=int(input("Enter number from 1-100: "))
while n!="guess":
    print
    if guess < n:
        print("Your guess is too low.")
        guess=int(input("Enter number from 1-100: "))
    elif guess > n:
        print("Your guess is too high.")
        guess=int(input("Enter number from 1-100: "))
    else:
        print("You guessed the right number!")
        break
        print


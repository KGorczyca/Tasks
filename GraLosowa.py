'''The rules of the game: the computer will come up with numbers from 0 to 100, and you must guess it '''



import random
my_number = random.randint(0,100)
guess = -1
trials = 0

print("Guess my number from 0 to 100")
while guess != my_number:
    guess = int(input())
    trials+=1
    if guess == my_number:
        print("Congratulations! You guessed the number for the",trials,"time")
    elif guess > my_number:
        print("Sorry - my number is smaller than your guess,try again!")
    else:
        print("Sorry - my number is greater than your guess, try again!")


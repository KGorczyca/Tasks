'''The rules of the game: the computer will come up with numbers from 0 to 100, and you must guess it '''



import random
import time

my_number = random.randint(0,100)
guess = -1
trials = 0

print("Guess my number from 0 to 100")
while guess != my_number:
    start_time = time.time()
    guess = int(input())
    trials+=1
    if guess == my_number:
        end_time = time.time()
        total_time = round(end_time-start_time,2)
        print("Congratulations! You guessed the number for the",trials,"time, and it takes:", total_time)
    elif guess > my_number:
        print("Sorry - my number is smaller than your guess,try again!")
    else:
        print("Sorry - my number is greater than your guess, try again!")


# Number Guessing Game.
# Importing random module for the program to randomly select a secret_number.

import random

# Define function number_guessin game.

def number_guessinggame():
    print("Guess a number between 1 and 100!")
    lowest_num = 1
    highest_num = 100
    secret_number = random.randint(lowest_num, highest_num) 
    attempts = 5
    
# A while loop to countinue asking the user untill they have guessed the correct number.

  while attempts > 0: 
      number = int(input("Entre a number between 1 and 100: ")  
# Control flow for the possible conditions
      if number < lowest_num or number > highest_num:
         print("Invalid Guess, Enter a valid input!")
      elif number < secret_number:
               print("Number is too low!")
      elif number > secret_number:
               print("Number is too high!")
      else:
         print(f"Congratulation you have guessed it in {attempts}")
         break
    attempts -= 1
    print(f"You have {attempts} guess left")
    print("Game Over\n")

if __name__ == "__main__":
   number_guessinggame()

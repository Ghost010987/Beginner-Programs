# Number Guessing Game.
# Importing random module for the program to randomly select a secret_number.

import random

# Define function number_guessin game.

def number_guessinggame():
    print("Guess a number between 1 and 100!")
    lowest_num = 1
    highest_num = 100
    secret_number = random.randint(lowest_num, highest_num) **# Using random.randint from the random module for the secret number.**
    guesses = 0
    
# A while loop to countinue asking the user untill they have guessed the correct number.

  while True:
       
  number = int(input("Entre a number between 1 and 100: "))  **# An input statement for the user to enter their response.** 
        guesses += 1 **# To count the number of guesses the user had to take to complete.**
        
# Control flow for the possible conditions

  if number < lowest_num or number > highest_num:
     print("Invalid Guess, Enter a valid input!")
  elif number < secret_number:
           print("Number is too low!")
  elif number > secret_number:
           print("Number is too high!")
  else:
     print("The guess is correct")
     print(f"Congratulations you guesed it in {guesses} attempts")
     break

if __name__ == "__main__":
   number_guessinggame()

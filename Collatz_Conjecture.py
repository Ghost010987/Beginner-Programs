# Collatz Sequence Program.
# Function collatz sequence is as follows:
def collatz_sequence(number):
    if number % 2 == 0:       # If the number as parameter is even number divide it by 2.
        return number // 2
    else:                     # If the number is an odd number the multiply it by 3 and add 1
        return 3 * number + 1
    
n = input("Enter a number: ") # User input to enter the number.
while n != 1:                 # A while loop to ensure the above function will run untill the number is reduced to 1.  
    n = collatz_sequence(int(n))

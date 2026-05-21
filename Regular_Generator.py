# Using a Generator to create data on the fly. 
# Make a function to generate mutiples with two parameters.
def generate_multiples(m, n):                 
    count = 0            # Let count be the default 0. 
    while count < n:     # A loop to iterate count n times.
        yield m * count  # So instead for return statement in a generator yield takes over.
        count += 1       # Incrementing count.

# This is the main function to generate output based on the above condition.
def main():
    m = int(input("Enter 'm' an integer value: ")) # User inputs for m and n respectively. 
    n = int(input("Enter 'n' an integer value: "))
    for mult in generate_multiples(m , n): # A for loop to iterate multiples. 
        print(mult, end=' ')
    print()

if __name__ == '__main__':  # Call the function.  
    main()

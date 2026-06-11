"""A code for overlapping Rotated Squares using turtle graphics"""

import turtle

# Create turtle object
t = turtle.Turtle()
t.speed(5) # Fastest drawing 

# Number of squares to draw
num_squares = 72 # 360/5 = 72 gives nice rotation

# Draw multiple squares
for _ in range(num_squares):
    for _ in range(4): # Draw a square
        t.forward(100)
        t.right(90)
    t.right(5)  # Rotate slightly before drawing next square

# Finish
turtle.exitonclick()
turtle.done()


# Reduction of rational number to the lowest term.
import math

class Rational_Number():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

def reduce(r):
        # Find the greatest common divisor of numerator and denominator
    g = math.gcd(r.numerator, r.denominator)

        # Divide the numerator and denominator with GCD
    r.numerator //= g
    r.denominator //= g

    return r # Return the reduced object

r = Rational_Number(10, 20)
r = reduce(r)
print(r)

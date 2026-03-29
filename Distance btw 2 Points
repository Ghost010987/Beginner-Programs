# Function to find distance between two points
import math
def dist_btw_points(P1, P2):
    x1 , y1 = P1
    x2 , y2 = P2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    try:
        P1 = input("Coordinates x1, y1: )
        P2 = input("Coordinates x2, y2: )
        P1_split = tuple(map(float, P1.split(",")))
        P2_split = tuple(map(float, P2.split(",")))
        print("Distance:", dist_btw_points(P1_split, P2_split))
    except ValueError:
        print("Invaid input. Please enter coordinates as "x,y")

if __name__ == "__main__":
    main()

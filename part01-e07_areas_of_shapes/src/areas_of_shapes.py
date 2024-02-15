#!/usr/bin/env python3

import math
           
def main():
    # enter you solution here
    shape=input("Choose a shape (triangle, rectangle, circle): ")

    while True:
        
        if shape == "":
            break

        elif shape == "circle":
            radius = float(input(f"Give radius of the {shape}: "))
            print(f"The area is {math.pi*radius**2}")

        elif shape == "rectangle":
            weight=float(input(f"Give weight of the {shape}: "))
            height=float(input(f"Give height of the {shape}: "))
            print(f"The area is {weight*height}")

        elif shape == "triangle":
            base=float(input(f"Give base of the {shape}: "))
            height=float(input(f"Give height of the {shape}: "))
            print(f"The area is {base*height/2}")
                
        else:
            print("Unknown shape!")
        
        shape=input("Choose a shape (triangle, rectangle, circle): ")

            
if __name__ == "__main__":
    main()

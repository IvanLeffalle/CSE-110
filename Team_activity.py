"""
Author: Ivan Leffalle
Project: Areas of Shapes
"""
#I used the Math library as a part 1 of the Stretch Challenge
import math

side = float(input("What is the length of a side of the square? "))
square = side ** 2 
print(f"The area of the square is: {square: .1f}")
length_rec = float(input("What is the length of rectangle? "))
width_rec = float(input("What is the width of the rectangle? "))
area_rec = length_rec * width_rec
print(f"The area of the rectangle is: {area_rec: .1f}")
radius_cir = float(input("What is the radius of the circle? "))
area_cir = math.pi * (radius_cir ** 2)
print(f"The area of the circle is: {area_cir: .4f}")
print("")

#Stretch Challenge part 2
single_value = float(input("please enter a single length value "))
square = single_value ** 2
circle = math.pi * (single_value ** 2)
cube_vol = single_value ** 3
sphere = (4/3) * math.pi * (single_value ** 3)

#display results
print(f"The area of the square is: {square: .1f}")
print(f"The area of the circle is: {circle: .1f}")
print(f"The volume of the cube is: {cube_vol: .1f}")
print(f"The volume of the sphere is: {sphere: .1f}")

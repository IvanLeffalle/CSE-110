def compute_area_square (side):
    area = side * side
    print(area)

def compute_area_rectangle (side1, side2):
    area = side1 * side2
    print(area)

def compute_area_circle (radius):
    area = 3.14 * (radius * radius)
    print(area)


shape = input("What kind of shape do you have? ")
    
while shape == "square":
        side = int(input("Enter the side value: "))
        compute_area_square(side)
        shape = input("What kind of shape do you have? ")
        
if shape == "rectangle":
            side1 = int(input("Enter the first side value: "))
            side2 = int(input("Enter the second side value: "))
            compute_area_rectangle(side1, side2)
            shape = input("What kind of shape do you have? ")

if shape == "circle":
            radius = float(input("Enter the radius value: "))
            compute_area_circle(radius)
            shape = input("What kind of shape do you have? ")
else:
     print("Thank you. Good bye")


#if shape.lower == "square":
 #2   compute_area_square

number = 6
UserNumberInput = input("Please guess the number: ")
UserNumber = int(UserNumberInput)

while UserNumber != number:
     if UserNumber < number:
         print("higher")   
     elif UserNumber > number:
         print("lower")
     UserNumberInput = input("Please guess the number: ")
     UserNumber = int(UserNumberInput)

print("You got it!")         


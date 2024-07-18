"""
Author: Ivan Leffalle
Project: Team Activity - Grade Calculator Program
"""
#Users will enter their grade
grade = float(input("Please enter your grade: "))
#will determine the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print("")
#will print the letter grade and tell the user if they passed the course or not
print(f"Your letter grade is: {letter}")
if grade >= 70:
    print("Congratulation you passed the course")
else:
    print("Sorry you have not passed the course, but prepare for next time")
    
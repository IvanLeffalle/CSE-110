"""
Author: Ivan Leffalle
Project: 02 Meal Price Calculator
"""
#I start by asking the user for information.
child_meal = float(input("What is the price of a child's meal?: "))
adults_meal = float(input("What is the price of an adult's meal?: "))
children = int(input("How many children are there?: "))
adults = int(input("How many adults are there?: "))
print("")

#Creativity: It will ask if the user want to add soda. 
#If the user answers "y". Then it will ask the price of the soda 
#and how many to add. Then it will add it to the subtotal.
#If the user answers "n" nothing except the meals will be added to the subtotal

soda_add = input("Add soda? y/n: ")
soda_sub = 0
if soda_add == "y":
    soda_price = float(input("What is the price of the soda?: "))
    soda_amount = float(input("How many sodas do you want to add?: "))
    soda_sub = soda_price * soda_amount  

#mathematical operations to obtain the subtotal
child_sub = child_meal * children
aduts_sub = adults_meal * adults
subtotal = child_sub + aduts_sub + soda_sub

#subtotal is displayed on the screen
print("")
print(f"Subtotal: ${subtotal: .2f}")
print("")
#assignment due for midweek ends

#asking the user the tax rate and calculating it
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * tax_rate / 100

#display the total
print(f"Sales Tax: ${sales_tax: .2f}")
total = subtotal + sales_tax
print(f"Total: ${total: .2f}")
print("")

#calculate the change
payment = float(input("What is the payment amount? "))
change = payment - total

#display the change
print(f"Change: ${change: .2f}")
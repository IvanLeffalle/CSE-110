shopping = []
print("Please enter the items of the shopping list (type: quit to finish):")
products = input("Item: ")

while products != "quit":
    shopping.append(products)
    products = input("Item: ")
print()
print ("The shopping list is:")
for item in shopping:
    print(item)
    
#2
print()
print("The shopping list with indexes is: ")

for i in range(len(shopping)):
    product = shopping [i]
    print (f"{i}- {product}")

#3
print()
remove = int(input("Which item would you like to change?: "))
new_product = input ("What is the new item?: ")

shopping[remove] = new_product
print()
print("The shopping list with indexes is: ")

for i in range(len(shopping)):
    product = shopping [i]
    print (f"{i}- {product}")


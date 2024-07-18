
"""
Author: Ivan Leffalle
Project: Shopping Cart
"""
#to Show Creativity I add the total number of product in the cart (line 31)
print("Welcome to the Shopping Cart Program!")
print("\nPlease select one of the following: ")
print("\n 1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit")
#first I prepared the lists, one for products and another for prices
cart = []
prices = []


selection = int(input("Please enter an action: "))

while selection != 5:
    if selection == 1:
        add = input("\nWhat item would you like to add?: ")
        cart.append(add)
        price = float(input(f"\nWhat is the price of {add}?: "))
        prices.append(price)
        print(f"'{add}' has been added to the cart")
        print("\nPlease select one of the following: ")
        print("\n 1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit")
        selection = int(input("Please enter an action: "))
        
#showing creativity
    elif selection == 2:
        total_items = len(cart)
        print(f"You have a total of {total_items} products in your cart.")     
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart)):
            item = cart[i]
            cash = prices[i]
            print(f"{i+1}- {item} - ${cash: .2f}")
        print("\nPlease select one of the following: ")
        print("\n 1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit")
        selection = int(input("Please enter an action: "))
    
    elif selection == 3:
        #I used -1 to make the list start at 1 instead of 0
        remove = int(input("Which item number would you like to remove? ")) - 1
        if 0 <= remove < len(cart):
                    removed_item = cart.pop(remove)
                    removed_price = prices.pop(remove)
                    print(f"'{removed_item}' has been removed from the cart")
        else:
                    print("Sorry, that is not a valid item number.")
        print("\nPlease select one of the following: ")
        print("\n 1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit")
        selection = int(input("Please enter an action: "))
    elif selection == 4:
          total = sum(prices)
          
          print(f"The total price of the items in the shopping cart is ${total}")
          print("\nPlease select one of the following: ")
          print("\n 1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit")
          selection = int(input("Please enter an action: ")) 
          
if selection == 5:
     print("Thank you. Goodbye") 




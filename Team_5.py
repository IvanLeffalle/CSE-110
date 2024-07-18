numbers = []
number =0
print("Enter a list of numbers, type 0 when finished.")
user_numbers = int(input("Enter number: "))
while user_numbers != 0:
    user_numbers = int(input("Enter number: "))
    if user_numbers != 0:
        numbers.append(user_numbers)
sum = 0
count = len(numbers)
for number in numbers:
    sum = number + number
average = sum / count
print(f"The sum is: {sum}")
print(f"The average is: {average}")






#print("the list is: ")
#for number in numbers:
    #print(number)


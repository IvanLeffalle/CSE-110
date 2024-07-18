age = int(input("How old are you?: "))
next_age = age + 1
print ("On your next birthday, you will be " + str(next_age))
print("")
eggs = int(input("How many egg cartons do you have?: "))
total_eggs = eggs * 12
print ("You have " + str(total_eggs) + " eggs")
print("")
cookies = int(input("How many cookies do you have?: "))
people = int(input("How many people are there?: "))

each_person = cookies / people

print(f"Each person may have {each_person} cookies")


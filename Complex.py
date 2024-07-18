print("Please answer using a rating from 1–10 on the following:")
print("")
loan = int(input("How large is the loan?: "))
history = int(input("How good is your credit history?: "))
income = int(input("How high is your income?: "))
payment = int(input("How large is your down payment?: "))

print("")
if (loan >= 5): 
    if history >= 7 and income >= 7:
        approved = True    
    elif  history >= 7 or income >= 7:
         if payment >= 5:
                approved = True
         else:
               approved = False
    else:
          approved = False
else:                  
    if history < 4:
     approved = False
    elif income >= 7 or payment >= 7:
        approved = True
    elif income == 4 and payment == 4:  
        approved = True  
    else:
          approved = False

    if approved:
         print("Decision: yes")

    else:
        print("Decision: no")






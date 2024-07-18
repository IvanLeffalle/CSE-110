
word  = "Commitment"

fav_let = input("please enter your favorite letter: ")


for letter in word:
    if letter.lower() == fav_let.lower():
           print (letter.upper(), end="")
    else:
             print (letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == fav_let.lower():
           print ("_", end="")
    else:
             print (letter.lower(), end="")

print()
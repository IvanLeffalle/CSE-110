friends = []

new_friend = input("Please type the name of a friend: ")
while new_friend != "end":
    friends.append(new_friend)
    new_friend = input("Please type the name of a friend: ")

for friend in friends:
    print(friend)




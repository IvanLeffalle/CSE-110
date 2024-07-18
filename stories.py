
#on line 22 I added an additional question to get user feedback.
print('Please enter the following:')
print()

adjective = input('adjective:')
animal = input('animal:')
verb = input('verb:')
exclamation = input('exclamation:')
verb = input('verb:')
verb = input('verb:')

print()
print('Your story is:')
print()

output = f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. "{exclamation.upper()}!" I yelled. But all I could think to do was to {verb} over and over. Miraculously, that caused it to stop, but not before it tried to {verb} right in front of my family.'

print(output)
print()

print('Please give me some feedback:')
print()
feedback = input('Do you like this story? (yes/no):')
if feedback == 'yes':
    print('That is awesome! I am glad you liked it.')
elif feedback == 'no' :
    print('I am sorry to hear that :( I will try to improve for the next time.')


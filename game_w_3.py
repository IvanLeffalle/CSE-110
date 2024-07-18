"""
Author: Ivan Leffalle
Title: Project 04: Word Puzzle
"""
print("Welcome to the word guessing game!")
print("")
SecretWord = "mosiah"
WordNumber = len(SecretWord)
hint = "_" * WordNumber
print(f"Your hint is: {hint}")

attempts = 0
UserGuess = input("Please guess the word: ")
# Check if the initial guess is correct
while SecretWord != UserGuess.lower():
    attempts += 1
    # Check if the length of the guess matches the length of the secret word
    if len(UserGuess) != WordNumber:
        print("Number of letters doesn't match")
        print()
    else:
         #Generate the new hint based on the guess
         new_hint = ""
         for i in range(WordNumber):
              if SecretWord[i] == UserGuess[i]:
                   new_hint += UserGuess[i].upper()
              elif UserGuess[i] in SecretWord:
                   new_hint += UserGuess[i].lower()
              else:
               new_hint += "_"
         hint = new_hint

 
         print(f"Your hint is: {hint}")
    UserGuess = input("Please guess the word: ")
                       
if SecretWord == UserGuess:
    print("You got it!")
    print(f"It took you {attempts} guesses.")



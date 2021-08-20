#needed this to pick a random word
from random import randint

userName = input('What\'s you\'re name?: ')
print(f'Welcome to Hangman {userName}!')

#These aren't the most creative words but oh well
wordList = ["Giraffe", "Philidelphia On Rocks", "Banana"]
#picking a random word from the 3
currentWord = wordList[1]

print('Let\'s get started!\n')

strikes = 0
#whether the user is done or not
#I set it to false to have something to keep my while loop going
completed = False

#the output list was made so I could replace values inside of it
outputList = []
output = ""
#adding the number of _ for the current word
for i in range(len(currentWord)):
    if currentWord[i]!=" ":
        outputList.append("_")
    else:
        outputList.append(" ")
#printing all of the underscores as a string
#each underscore has a space after it to make it look better
for i in outputList:
    output += i
    output += " "
print(output)

userGuess = input("Enter a character: ")
while completed != True:
    #this makes sure that they type in a single letter
    while (userGuess.isalpha() == False) or (len(userGuess) > 1):
        print("Invalid input!")
        userGuess = input("Enter a character: ")
    #the .lower() makes sure that the user can type in capital or lowercase and still get the guess right
    if userGuess.lower() in currentWord.lower():
        print('Good Guess!\n')
        #resetting the output to print my new one with the updated list
        output = ""
        #this for loop replaces the index in the output list with what the user got right
        for i in range(len(currentWord)):
            if currentWord[i].lower() == userGuess.lower():
                outputList[i] = currentWord[i]
        #printing out my output again as a string
        for i in outputList:
            output += i
            output += " "
        print(output)
        print(f"Strikes: {strikes}")
    elif userGuess not in currentWord:
        #6 strikes max
        strikes += 1
        print('Oops! Try Again.\n')
        print('+1 Strike')
        print(f'{strikes}/6 strikes')
        #breaks the while loop if the get 6 strikes
        if strikes == 6:
            break
    #this is a check for whether the user is done or not
    #if they have no more guesses left, then it breaks the loop
    if "_" not in output:
        completed = True
        break
    elif "_" in output:
        userGuess = input("Enter a character: ")

#this is a check for if they won or lost based on strikes
#since there are 2 breaks in the while loop above, one for winning and one for losing
if strikes == 6:
    print("You lost!")
elif strikes != 6:
    print("You won!")

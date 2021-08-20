from random import randint
import random
import string

#i went ahead and did this because i was bored
historyList = []

retry = "y"
while retry == "y" or retry == "yes":
    capLetters = int(input('# of capital letters: '))
    lowerLetters = int(input('# of lowercase letters: '))
    numbers = int(input('# of numbers: '))
    symbols = int(input('# of symbols: '))

    passwordRaw = ""

    #to only include symbols from the row above top (1-0)
    symbolsAdd = 0

    #appending all of the things to the list first
    for i in range(capLetters):
        passwordRaw += chr(randint(65,90))

    for i in range(lowerLetters):
        passwordRaw += chr(randint(97,122))

    for i in range(numbers):
        passwordRaw += chr(randint(48,57))

    while symbols != 0:
        symbolsAdd = randint(33,64)
        #"semantic" if statements
        #https://stackoverflow.com/questions/16830793/how-to-shorten-long-and-statements
        if symbolsAdd == 33 \
        or symbolsAdd == 35 \
        or symbolsAdd == 36 \
        or symbolsAdd == 37 \
        or symbolsAdd == 38 \
        or symbolsAdd == 40 \
        or symbolsAdd == 41 \
        or symbolsAdd == 42 \
        or symbolsAdd == 64:
            passwordRaw += chr(symbolsAdd)
            symbols -= 1

    #shuffling the string so it is randomized
    #SOURCE: https://note.nkmk.me/en/python-random-shuffle/
    password = ''.join(random.sample(passwordRaw, len(passwordRaw)))
    print(password)
    historyList.append(password)

    retry = input('\nRetry? (y/n/h (history)): ')

#after the while loop is broken
#prints the historyList vertically or See ya 'round if they chose not to print the history
historyOutput = ""
if retry == "h" or retry == "history":
    print("Generated password: ")
    for j in historyList:
        print(j)
elif retry == "n" or retry == "no":
    print('See ya \'round!')
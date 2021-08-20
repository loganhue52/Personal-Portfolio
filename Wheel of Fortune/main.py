import time
from random import randint
from Wheel import Wheel
from Puzzle import Puzzle

#for clearing the console
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#function to rotate through players
def nextplayer(currentplayer,pllist):
    if currentplayer==pllist[0]:
        currentplayer=pllist[1]
    elif currentplayer==pllist[1]:
        currentplayer=pllist[2]
    elif currentplayer==pllist[2]:
        currentplayer=pllist[0]
    return currentplayer

print('Welcome to Wheel of Fortune! I\'m Pat Sajak and this is Vanna White!')

player1=input('Player 1\'s Name: ')
player2=input('Player 2\'s Name: ')
player3=input('Player 3\'s Name: ')

#list of the players
pllist=[player1,player2,player3]
#player amounts(temp)
pamts=[0,0,0]
#player totals(permanent)
ptotals=[0,0,0]

#randomlyt picks a player
currentplayer=pllist[randint(0,2)]

wheel=Wheel.makeWheel(None)

#puzzles and catagories
#will always go from 0 to 3
puzzlelist=['Empire State Building','Picnic Basket','An Arm and a Leg',    'Baking a Cake'     ]
catagories=[       'Place'         ,    'Thing'    ,     'Phrase'     , 'What are you doing?'  ]

currentpuzzle=puzzlelist[0]
currentcat=catagories[puzzlelist.index(currentpuzzle)]

puzzle=Puzzle(currentpuzzle)
puzzle.makePuzzle()

round=1
switchplayer=False
switchround=False
firstturn=[True,True,True]

#while loop for rounds
while round<5:

    #checking to see if round should be switched
    if "_" not in str(puzzle):
        switchround=True
    #resets everything with a new puzzle
    if switchround==True:
        currentpuzzle=puzzlelist[puzzlelist.index(currentpuzzle)+1]
        puzzle=Puzzle(currentpuzzle)
        puzzle.makePuzzle()
        round+=1
        for i in range(len(pamts)):
            ptotals[i]=ptotals[i]+pamts[i]
        pamts=[0,0,0]
        switchround=False
        print('New Puzzle on the Board!')

    if switchplayer==True:
        currentplayer=nextplayer(currentplayer,pllist)
        print('Next player...')
        time.sleep(1)
        switchplayer=False

    print(f'It\'s {currentplayer}\'s turn.')

    #while loop for each players turn
    while switchplayer==False and puzzle.iscomplete()==False:

        print(f'''
        Puzzle on the Board:
        {puzzle}''')

        spin=Wheel.spin(wheel)

        #did these spins first to get the string values out of the way
        print(f'Player {currentplayer} spin: {spin}')
        if spin=='Bankrupt':
            print('Welp there goes your money... Next player\'s turn.')
            pamts[pllist.index(currentplayer)]=0
            switchplayer=True
        elif spin=='Lose A Turn':
            print('Ooooooh sorry about that... Next player\'s turn.')
            switchplayer=True
        elif spin=='Free Play':
            print('Free play!')
            uI=input('Letter to Guess (Consonant or Vowel): ')
            if puzzle.replace(uI)==None:
                print('Sorry, that letter isn\'t in the puzzle!')
                switchplayer=True
            else:
                cls()
                print('Good guess!')
                print(f'''
        Puzzle on the Board:
        {puzzle}''')
        #else if the spin was a number
        else:
            #add to temp amount
            pamts[pllist.index(currentplayer)]=pamts[pllist.index(currentplayer)]+spin
            #while loop until the player guesses wrong
            while True and puzzle.iscomplete()==False:
                print(f'''
        Bank:
        {player1}: {pamts[0]}
        {player2}: {pamts[1]}
        {player3}: {pamts[2]}''')
                uI=input('What would you like to do?\n1. Guess a consonant\n2. Buy a vowel\n> ')
                if "1" in uI or "con" in uI.lower():
                    uI=input('Letter to Guess: ')
                    #using this in a conditional calls it and replaces the letter, no need to call it later
                    if puzzle.replace(uI)==None:
                        print('Sorry, that letter isn\'t in the puzzle!')
                        switchplayer=True
                        break
                    else:
                        cls()
                        print('Good guess!')
                        print(f'''
        Puzzle on the Board:
        {puzzle}''')
                        #add consonant value to temp amount
                        pamts[pllist.index(currentplayer)]=pamts[pllist.index(currentplayer)]+spin
                else:
                    #makes sure the player has money
                    if (pamts[pllist.index(currentplayer)]-250)<0:
                        print('You don\'t have enough money!')
                        switchplayer=True
                        break
                    #if they do, subtract 250
                    else:
                        pamts[pllist.index(currentplayer)]=pamts[pllist.index(currentplayer)]-250
                        uI=input('Letter to Guess: ')
                        if puzzle.replace(uI)==None:
                            print('Sorry, that letter isn\'t in the puzzle!')
                            switchplayer=True
                            break
                        else:
                            cls()
                            print('Good guess!')
                            print(f'''
        Puzzle on the Board:
        {puzzle}''')
                            
cls()
print(f'''
Thank you all for playing!
Here are the final winnings:
{player1}: {ptotals[0]}
{player2}: {ptotals[1]}
{player3}: {ptotals[2]}
''')
        
        
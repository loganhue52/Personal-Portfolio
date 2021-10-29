from random import randint
import random
import string
import sys
from Generator import Generator
from Checker import Checker

catDictionary={}

def addCatagory():
    uI=input('Catagory Name: ')
    #making the stored dictionary values a list so i can remove specific indices
    catDictionary[uI] = []

def listFunc():
    #for every key (the catagories) in the dictionary, print (catagory):
    for i in catDictionary.keys():
        print(i,":")

        #this conditional was to fix the issue of printing out one vs multiple values
        #if the value is a list, it iterates through the list
        #if it isnt, it just prints that value
        #Credit to Gaege for this one
        if type(catDictionary[i]) == list:
            for j in catDictionary[i]:
                print("\t",j)
            print()
        else:
            print("\t",catDictionary[i])
            print()

def addPass():
    #this placed variable was a debug thing i did but decided to keep because it works
    placed=False
    #telling the user the requirements
    print('New password must have:\n\t1 capital letter\n\t1 number\n\t1 special symbol: !,@,#,$,%,^,&,(,)\n\tLength of 8 or more')
    newPass=input('New password: ')
    #this makes sure that they enter a password that meets the requirements
    while Checker(newPass).check()==False:
        print('New password does not meet the requirements!')
        newPass=input('New password: ')
    print('Please select a catagory to add your password to.\n(use "ls" to list catagories and passwords.)')
    while placed==False:
        #wasn't sure if i should keep this but i did
        uI=input('> ')
        if uI=="ls":
            listFunc()
            uI=input('> ')
        #makes sure that the catagory the user chose was an actual catagory
        if uI in catDictionary.keys():
            catDictionary[uI].append(newPass)
            placed=True
        else:
            print('Invalid catagory, try again.')
    #print(catDictionary)

def remPass():
    while True:
        x = 0
        uCat = input('Catagory Name: ')
        if fillCheck(catDictionary[uCat]) == False:
            print('There are no passwards in this catagory!')
            return
        if uCat in catDictionary.keys():
            if type(catDictionary[uCat]) == list:
                for i in catDictionary[uCat]:
                    x+=1
                    print(f'{x}.',i)
                break
            else:
                print("1.",catDictionary[uCat])
                break
        else:
            print('Invalid catagory')
    uI=input('Select the password to remove: ')
    #couldn't figure out how to remove specific values from a dictionary key, so i made the values for the dict a list
    k = int(uI)-1
    #the user can either put in the exact password or the number cooresponding to it
    #the following conditional is for if they entered a number or the exact password
    if uI in catDictionary[uCat]:
        # i = str(catDictionary[uCat])
        indice=int(catDictionary[uCat].index(uI))
        catDictionary[uCat] = catDictionary[uCat][:indice]+catDictionary[uCat][indice+1:]
    elif catDictionary[uCat][k] != "":
          catDictionary[uCat] = catDictionary[uCat][:k]+catDictionary[uCat][k+1:]
    else:
        print('Invalid Input')

def editPass():
    while True:
        x=0
        uCat = input('Catagory Name: ')
        if fillCheck(catDictionary[uCat]) == False:
            print('There are no passwards in this catagory!')
            #copied code from the remPass() function
            return
        if uCat in catDictionary.keys():
            if type(catDictionary[uCat]) == list:
                for i in catDictionary[uCat]:
                    x+=1
                    print(f'{x}.',i)
                break
            else:
                print("1.",catDictionary[uCat])
                break
        else:
            print('Invalid catagory')
    
    uI=input('Select the password to edit: ')
    changeIn=input('Type what you want it changed to: ')
    while Checker(changeIn).check()==False:
        print('New password does not meet the requirements!')
        changeIn=input('Changed password: ')
    k = int(uI)-1
    #most of this function is copied from the remPass() function but instead of removing, it replaces
    if uI in catDictionary[uCat]:
        indice=int(catDictionary[uCat].index(uI))
        catDictionary[uCat][indice] = str(changeIn)
    elif catDictionary[uCat][k] != "":
          catDictionary[uCat][k] = str(changeIn) 
    else:
        print('Invalid Input')

#this function makes sure that there are values in what is passed in
def fillCheck(i):
    if str(i) == "":
        return False
    elif i == {}:
        return False
    elif i == []:
        return False
    else:
        return True

logIn=False
askNewUser=input('Are you a new user? (y/n): ')
masterPass="p4$$w0rD"
if "y" in askNewUser.lower():
    userFName=input('First Name: ')
    userLName=input('Last Name: ')
    userUName=input('Username: ')
    print('New password must have:\n\t1 capital letter\n\t1 number\n\t1 special symbol: !,@,#,$,%,^,&,(,)\n\tLength of 8 or more')
    masterPass=input('Master Password: ')
    while Checker(masterPass).check()==False:
        print('New password does not meet the requirements!')
        masterPass=input('Master Password: ')
    print("Account created!")

tries = 3
while logIn==False:
    uI=input('Enter Master Password: ')
    if uI == masterPass:
        logIn = True
        print('Log In Successful!')
    elif uI != masterPass:
        print('Log In Failed')
        tries -= 1
        print(f'{tries} tries remaining.')
        #completely shuts down the program when they fail
    if tries == 0:
        print('Exiting...')
        sys.exit()
    
#print('Welcome.')

uI=""
while uI!="quit":
    #wanted to go for a more console-esk feel, like a command prompt password manager and less like an "app"
    print('''
    Commands:
        ac - add catagory
        ls - list catagories and passwords
        ap - add password
        rp - remove password
        ep - edit password
        gp - generate password
        quit - exit
    ''')
    uI = input('> ')
    #these are all of my checkers to run fuctions when the user inputs a command
    if "ac" in uI.lower():
        addCatagory()
    elif "ls" in uI.lower():
        listFunc()
    elif "ap" in uI.lower():
        if fillCheck(catDictionary) == False:
            print('Please create a catagory first!')
        else:
            addPass()
    elif "rp" in uI.lower():
        if fillCheck(catDictionary) == False:
            print('Please create a catagory first!')        
        remPass()
    elif "ep" in uI.lower():
        if fillCheck(catDictionary) == False:
            print('Please create a catagory first!')
        editPass()
    elif "gp" in uI.lower():
        print(f'Generated password: {Generator().generate()}')
    elif "q" in uI:
        sys.exit()
    else:
        print('Invalid input')


#retry = "y"
#historyList = []
# historyOutput = ""
# if retry == "h" or retry == "history":
#     print("Generated password: ")
#     for j in historyList:
#         print(j)
# elif retry == "n" or retry == "no":
#     print('See ya \'round!')

#masterList = ["home","work","entertainment","bills"]
#userInput=""
# while(userInput!="quit"):
#     print("comand inputs are\n\taddfolder - this adds a folder to the database\n\tgotofolder - this takes you to the folder that you type in.\n\taddpass - this adds a password to the folder of your chose\n\tquit - this logs you out of the program")
#     userInput=input("")
#     if userInput=="addfolder":
#         addFolderInput=input("What is the name of the folder you want to create? ")
#         masterList.append(addFolderInput)
#         print(masterList)
#     elif userInput=="gotofolder":
#         print("folders:",", ".join(masterList))
#         folder=input("Type in the folder that you want to go to? ")
#         if folder in masterList:
#             print(f"you are in the {folder} folder")
            
#     elif userInput=="addpass":
#         pickfolder=input("Chose a folder to store the password in from the following "+", ".join(masterList)+" ")
#         if pickfolder in masterList:
#             ui=input("what is the name of the website you are using the password for? ")
#             addpass=input("type in the password for it. ")
#             masterList.insert(0,ui)
#             masterList.append(addpass)
#             print(masterList)
menu=('''
   _____          _      _      ________     __   _____ _____  _    _ ____  
  / ____|   /\\   | |    | |    |  ____\\ \\   / /  / ____|  __ \\| |  | |  _ \\ 
 | |  __   /  \\  | |    | |    | |__   \\ \\_/ /  | |  __| |__) | |  | | |_) |
 | | |_ | / /\\ \\ | |    | |    |  __|   \\   /   | | |_ |  _  /| |  | |  _ < 
 | |__| |/ ____ \\| |____| |____| |____   | |    | |__| | | \\ \\| |__| | |_) |
  \\_____/_/    \\_\\______|______|______|  |_|     \\_____|_|  \_\\\\____/|____/ 
_____________________________________________________________________________
          Krabby Patty.........$1.25    Krabby Meal.........$3.50
            w/ sea cheese......$1.50    Double Krabby Meal..$3.75
          Double Krabby Patty..$2.00    Triple Krabby Meal..$4.00
            w/ sea cheese......$2.25    Salty Sea Dog.......$1.25
          Triple Krabby Patty..$3.00    Footlong............$2.00
            w/ sea cheese......$3.25    Sailor's Surprise...$3.00
                                        Golden Loaf.........$2.00
          Coral Bits                      w/ sauce..........$2.50
            Small..............$1.00
            Medium.............$1.25    Kelp Shake..........$2.00
            Large..............$1.50          Seafoam Soda
                                            Small.......$1.00
          Kelp Rings...........$1.50        Medium......$1.25
              salty sauce......$0.50        Large.......$1.50
''')

import sys
#using a 2d list for the menu selections
menuList = [["krabby meal", "double krabby meal", "triple krabby meal", 
"salty sea dog","footlong", "sailor's surprise", "sailors surprise", "kelp shake"],
["krabby patty","double krabby","triple krabby patty"],
["seafoam soda","coral bits"]]
total = 0.00
#the more i use dictionaries, the more i dont like them - however they are useful
#ive found it is easier to use dictionaries when there is a single key:value pair and the value is a list that you can manipulate
orderList = {}
orderNumber = 1
#this function is called adder because it appends dictionary values and adds to the total
def adder(userInput):
  global total
  if userInput.lower() in menuList[1]:
    sCheeseInput=input('Would you like sea cheese with that?: ')
    if "y" in sCheeseInput.lower():
      total += 0.25
      #making sure that the user sees that they ordered sea cheese with it
      orderList[str(orderNumber)].append("sea cheese")
    if "double" in userInput.lower():
      total += 2.00
    elif "triple" in userInput.lower():
      total += 3.00
    else:
      total += 1.25
      #.title() is used to make it look better
    orderList[str(orderNumber)].append(userInput.title())
  elif userInput.lower() in menuList[2]:
    sizeInput=input('Small, Medium, or Large?: ')
    if sizeInput.lower()=="small":
      total += 1.00
    elif sizeInput.lower()=="medium":
      total += 1.25
    elif sizeInput.lower()=="large":
      total += 1.50
      #making sure that there is the item and the size
    orderList[str(orderNumber)].append(sizeInput.title()+" "+userInput.title())
  elif userInput.lower() in menuList[0]:
    if "double" in userInput.lower():
      total += 3.75
    elif "triple" in userInput.lower():
      total += 4.00
    elif "salty" in userInput.lower():
      total += 1.25
    elif "foot" in userInput.lower():
      total += 2.00
    elif "surprise" in userInput.lower():
      total += 3.00
    elif "shake" in userInput.lower():
      total += 2.00
    else:
      total += 3.50
      #yes i do realize i could have iterated through the list
    orderList[str(orderNumber)].append(userInput.title())
  elif "golden" in userInput.lower():
    sInput = input('Would you like sauce with that?')
    if "y" in sInput.lower():
      total += 2.50
      #so the user knows they ordered sauce:
      orderList[str(orderNumber)].append(userInput.title()+" w/ sauce")
    else:
      total += 2.00
      orderList[str(orderNumber)].append(userInput.title())
  elif "rings" in userInput.lower():
    sInput = input('Would you like salty sauce with that?')
    if "y" in sInput.lower():
      total += 2.00
      orderList[str(orderNumber)].append(userInput.title()+" w/ salty sauce")
    else:
      total += 1.50
      orderList[str(orderNumber)].append(userInput.title())
  else:
    print('Wrong Input')

def listFunc():
      #this bit of code is shared between here and the password manager
      #the orderList being a dictionary was a last minute change
      #this used to be a huge function iterating through a 2D list that gave me a headache
  for i in orderList.keys():
        print("Order",i,":")
        if type(orderList[i]) == list:
            for j in orderList[i]:
                print("\t",j)
            print()
        else:
            print("\t",orderList[i])
            print()

def taxes(t):
      #i want the user to see exactly how the total is added up, so I included all three of these in their order
  orderList[str(orderNumber)].append(f"Subtotal: ${total}")
  tax = total*0.07
  tax = round(tax, 2)
  orderList[str(orderNumber)].append(f"Tax: ${tax}")
  newTotal = total*1.07
  newTotal = round(newTotal,2)
  orderList[str(orderNumber)].append(f"Total: ${newTotal}")

#the beginning of the actual running code
print(menu)
userInput = input('What can I get for you? (quit to exit): ')
#the user can type "quit" at any time and it will stop the program and print out the orders
while userInput.lower() != "quit":
      #making sure the current order is a key in the dictionary
  if str(orderNumber) not in orderList.keys():
        #had to convert orderNumber to a str or it would throw a keyError
    orderList[str(orderNumber)] = []
  adder(userInput)
  print(f'Current total: ${total}')
  userInput = input('Anything else for this order?: ')
  #this bit may seem weird but it makes perfect sense in my head
  if "no" in userInput.lower():
        #appending the order total so that each order has its own total
    #print(f'Orders: \n{listFunc()}')
    taxes(total)
    listFunc()
    userInput = input('Would you like to place another order? (yes/no): ')
    #there was a bug here where you could type what you want when it asked if you wanted to place another order and it would be 
    #really messed up after wards
    #fixed it with a while loop
    while True:
      if "yes" in userInput.lower():
            #resetting the total and adding another order key to the dict
        total = 0
        orderNumber += 1
        userInput = input('What can I get for you? (quit to exit): ')
        break
      elif "no" in userInput.lower():
        #printing the orders and ending the program
        listFunc()
        sys.exit()
      else:
        print('Wrong Input')
        userInput = input('Would you like to place another order? (yes/no): ')


listFunc()
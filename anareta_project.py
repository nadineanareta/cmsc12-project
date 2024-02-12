# ANARETA, Nadine Arabel A.
# CMSC 12 - E3L
# Farm2Market Game
'''
ADDITIONAL FEATURES:
[1] Inputs and saves ID of the player: single-player only
[2] Cannot proceed with an incorect password
[3] Indicates or prints the updates of every wallet, inventory, and farm layout data for the user to see
[4] Has a hidden or cheat code just like every other game
[5] Indicates the harvest time of each crop or livestock
[6] Auto-saves the data for all features of the game
[7] Includes missions for planting, harvesting, or buying crops and livestocks
[8] Full of prizes and gifts as the user plays
'''

from datetime import datetime, timedelta # importing datetime module
ID = {} # dictionary containing the allotted wallet and will be containing the ID of the player
Inventory = {} # dictionary of the items bought 
Sell= {} # dictionary of the items sold
farm_layout = {} # dictionary of the farm_layout, class type <str>
farm_layout_1 = {} # dictionary of the time planted and harvest time
plant_m = {} # dictionary for the plant mission
harvest_m = {} # dictionary for the harvest mission
buy_m = {} # dictionary for the buy mission

# load function for the ID
def load_wallet(inven):
    inven = {} #empty dictionary
    elements = [] #empty list
    fh = open("anareta1.txt", "r")
    for line in fh:
        elements.append(line[:-1]) #list of lines

    kpair1 = elements[0] # Wallet
    values1 = int(elements[1]) # Wallet value
    kpair2 = elements[2] # Name
    values2 = elements[3] # Name value
    kpair3 = elements[4] # Sign
    values3 = int(elements[5]) # Sign value
    inven[kpair1] = values1
    inven[kpair2] = values2
    inven[kpair3] = values3
    fh.close()
    return inven

# save function for the ID
def save_wallet(inven):
    fh = open("anareta1.txt", "w")
    for k, v in inven.items():
        fh.write(k +"\n")
        fh.write(str(v) +"\n")
    fh.close()
    return inven 

# load function for the inventory
def load_inven(invent):
    invent = {} # empty dictionary
    elements = [] # empty list
    fh = open("anareta2.txt", "r")
    for line in fh:
        elements.append(line[:-1]) #list of lines
    for i in range(0, len(elements), 2):
        kpair1 = elements[i] # inventory keys
        values1 = int(elements[i+1]) # inventory values
        invent[kpair1] = values1
    fh.close()
    return invent

# save function for the inventory
def save_inven(invent):
    fh = open("anareta2.txt", "w")
    for k, v in invent.items():
        fh.write(str(k) + '\n')
        fh.write(str(v) + '\n')
    fh.close()
    return invent

# load function for the sold items
def load_sell(sell):
    sell = {} # empty dictionary
    elements = [] # empty list
    fh = open("anareta3.txt", "r")
    for line in fh:
        elements.append(line[:-1]) # list of lines
    for i in range(0, len(elements), 2):
        kpair1 = elements[i] # keys
        values1 = int(elements[i+1]) #values
        sell[kpair1] = values1
    fh.close()
    return sell

# save function for the sold items
def save_sell(sell):
    fh = open("anareta3.txt", "w")
    for k, v in sell.items():
        fh.write(str(k) + '\n')
        fh.write(str(v) + '\n')
    fh.close()
    return sell

# load function for the farm lot
def load_farm(farm_lot):
    farm_lot = {} # empty dictionary
    elements = [] # empty list
    fh = open('anareta4.txt', 'r')
    for line in fh:
        elements.append(line[:-1]) # list of lines
    for i in range(0, len(elements), 2):
        key = int(elements[i]) # keys
        value = elements[i+1] # values
        if value[0] == '[':
            value = value[1:-1] # gets the values in the list
            value = value.split(', ') # splits the values in the list
            value[0] = value[0][1:-1] #disregarding the '' in the string
            value[1] = value[1][1:-1]
            value[2] = value[2][1:-1]
            value[3] = value[3][1:-1]

        farm_lot[key] = value # updates the dictionary

    fh.close()
    return farm_lot

# save function for the farm lot
def save_farm(farm_lot):
    fh = open('anareta4.txt', 'w')
    for k, v in farm_lot.items():
        fh.write(str(k) + '\n')
        fh.write(str(v) + '\n')
    fh.close()
    return farm_lot

# function that converts string to datetime
def convert(string):
    date_now = datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')
    return date_now

# load function for the time in farm lot
def load_dfarm(dfarm_lot):
    dfarm_lot = {} # empty dictionary
    elements = [] # empty list
    fh = open('anareta5.txt', 'r')
    for line in fh:
        elements.append(line[:-1]) # lines in list
    for i in range(0, len(elements), 3):
        key = int(elements[i]) # key
        value = elements[i+1] # first value
        value1 = elements[i+2] # second value
        kvalue = [value, value1]
        dfarm_lot[key] = kvalue # dictionary
    
    for key, kvalue in dfarm_lot.items():
        if kvalue[0] == 'Empty' and kvalue[1] == 'Empty': # checks if farm block is empty
            None
        else:
            dfarm_lot[key][0] = convert(dfarm_lot[key][0]) # converts into datetime
            dfarm_lot[key][1] = convert(dfarm_lot[key][1]) # converts into datetime

    fh.close()
    return dfarm_lot

# save function for the time in farm lot
def save_dfarm(dfarm_lot):
    fh = open('anareta5.txt', 'w')
    for k, v in dfarm_lot.items():
        if v == 'Empty': # checks if the farm block is empty
            fh.write(str(k) + '\n')
            fh.write('Empty' + '\n')
            fh.write('Empty' + '\n')
        else:
            fh.write(str(k) + '\n')
            fh.write(str(v[0]) + '\n')
            fh.write(str(v[1]) + '\n')
    fh.close()
    return dfarm_lot

# load function for the plant mission
def load_plantm(invent):
    invent = {} # empty dictionary
    elements = [] # empty list
    fh = open("anareta6.txt", "r")
    for line in fh:
        elements.append(line[:-1]) #list of lines
    for i in range(0, len(elements), 2):
        kpair1 = elements[i] # keys
        values1 = int(elements[i+1]) # values
        invent[kpair1] = values1
    fh.close()
    return invent

# save function for the plant mission
def save_plantm(invent):
    fh = open("anareta6.txt", "w")
    for k, v in invent.items():
        fh.write(str(k) + '\n')
        fh.write(str(v) + '\n')
    fh.close()
    return invent

# load function for the harvest mission
def load_harvestm(invent):
    invent = {} # empty dictionary
    elements = [] # empty list
    fh = open("anareta7.txt", "r")
    for line in fh:
        elements.append(line[:-1]) #list of lines
    for i in range(0, len(elements), 2):
        kpair1 = elements[i] # keys
        values1 = int(elements[i+1]) # values
        invent[kpair1] = values1
    fh.close()
    return invent

# save function for the harvest mission
def save_harvestm(invent):
    fh = open("anareta7.txt", "w")
    for k, v in invent.items():
        fh.write(str(k) + '\n')
        fh.write(str(v) + '\n')
    fh.close()
    return invent

# load function for the buy mission
def load_buym(invent):
    invent = {} # empty dictionary
    elements = [] # empty list
    fh = open("anareta8.txt", "r")
    for line in fh:
        elements.append(line[:-1]) #list of lines
    for i in range(0, len(elements), 2):
        kpair1 = elements[i] # keys
        values1 = int(elements[i+1]) # values
        invent[kpair1] = values1
    fh.close()
    return invent

# save function for the buy mission
def save_buym(invent):
    fh = open("anareta8.txt", "w")
    for k, v in invent.items():
        fh.write(str(k) + '\n')
        fh.write(str(v) + '\n')
    fh.close()
    return invent

# welcome message
def welcomemsg():
    print("================= Welcome to Farm2Market =================")
    print('''This is a farm simulation game. You'll play the role of 
a farmer in this game. You are given an initial amount 
of Php 10,000 as a budget for your farm. 

[1] There are hidden cheat codes within the game. Make sure 
to explore the game and learn all of them.
[2] Includes mission for you to enjoy and amazing 
prizes if you compete any of those.

That is all.... Good luck and Enjoy!''' + '\n') #description of the game

# function that inputs the password or name of the player == only accepts ONE player
def inputID():
    name_id = input("Enter password: ")
    if name_id not in ID.values(): # if the input password is incorrect
        print('\n' + name_id + " is an incorrect password.")
        print("[1] Input again")
        print("[0] Exit" + '\n')
        new_game = input("Enter choice: ")
        if new_game == '1':
            name_id = input("Enter password: ")
            if name_id not in ID.values(): # if the input ID is STILL incorrect
                print(name_id,"has not been saved in the game. Input again.")
                print("------------------------------------------------------"+ '\n')
                inputID()
            else: # welcome message after the ID input
                print('\n' + f"Welcome, {name_id}! Your farm is waiting for you. Go have some fun!")
                print("------------------------------------------------------"+ '\n') 
                ID['Sign'] += 1
        elif new_game == '0':
            exit() # exit function of the game
            quit()
        else:
            print("Invalid Input")
            print("---------------" + '\n')
            inputID()
    else: # welcome message after the ID input
        print('\n' + f"Welcome, {name_id}! Your farm is waiting for you. Go have some fun!")
        print("------------------------------------------------------"+ '\n')
        ID['Sign'] += 1
    
    save_wallet(ID)

# function for signing in
def sign_in():
    if ID['Sign'] == 3:
        print("You have currently signed in the game thrice.")
        print("Receive Php 100 as a gift. Thank you and enjoy!" + '\n')
        ID['Wallet'] += 100
    elif ID['Sign'] == 10:
        print("You have currently signed in the game 10 times.")
        print("Receive Php 200 as a gift. Thank you and enjoy!" + '\n')
        ID['Wallet'] += 200 
    elif ID['Sign'] == 15: 
        print("You have currently signed in the game 15 times.")
        print("Receive Php 500 as a gift. Thank you and enjoy!" + '\n')
        ID['Wallet'] += 500
    elif ID['Sign'] == 20:
        print("You have been an avid player since you signed in 20 times already.")
        print("Receive Php 1,000 as a gift. Thank you and enjoy!" + '\n')
        ID['Wallet'] += 1000

    save_wallet(ID)   

# function for main menu
def mainmenu():
    print('\n' + "==================== MAIN MENU ====================")
    print("[1] Visit My Farm Lot")
    print("[2] Visit Item Shop")
    print("[3] View Inventory")
    print("[4] Plant Seeds and Tend Livestocks")
    print("[5] Sell Farm Produce")
    print("[6] View Missions")
    print("[0] Exit Game" + '\n')

# function for the farm lot
def farmlot():
    if Inventory["Farm Blocks"] == 0: # checks if the user alredy owned a farm lot or not
        print('\n' + "================ FARM LAYOUT ================")
        print("No farm layout.")
        print("----------------------------------------")
    else: # if the user already has bought a farm lot
        print('\n' + "================ FARM LAYOUT ================")
        blocks = Inventory["Farm Blocks"]
        i = 1
        while blocks > 0: # prints the farm lot
            if farm_layout[i] == 'Empty':
                print(f"[{i}] [--] [--]")
            else:
                print(f"[{i}] [{farm_layout[i][1]}] [Time planted: {farm_layout[i][2]}]")
            blocks -= 1
            i += 1
        farmlot_inner()

# function for the options in farm lot
def farmlot_inner():
    while True: # continuous choice
        print('\n' + "[1] View my crops and livestocks")
        print("[2] Harvest crops and livestocks")
        print("[0] Go back to main menu" + '\n')
        farmlot_choice = input("Enter choice: ")
        if farmlot_choice == '1': # prints ONLY the farm blocks with planted seeds or livestocks and their harvest time
            for k, v in farm_layout.items():
                if v != 'Empty':
                    print(f"[{k}] [{farm_layout[k][1]}] [Harvest Time: {farm_layout[k][3]}]")
        elif farmlot_choice == '2': # choice for harvesting
            harvest_now = datetime.today() # gets the current time
            harvest_choice = input("Enter initial farm block: ")
            harvest = farm_layout[int(harvest_choice)][0] # classification of the crop or livestock
            time_harvest = farm_layout_1[int(harvest_choice)][1] # gets the time to harvest
            if farm_layout[int(harvest_choice)] != 'Empty': # checks first if the block is empty
                left_harvest = time_harvest - harvest_now # subtracts the current time from the time of harvest
                if harvest_now < time_harvest: # checks if farm block is ready for harvest
                    print('\n' + f"{harvest} is not yet ready for harvest.")
                    print(f'{left_harvest} left before it could be harvested.')
                    print('------------------------------------------')
                else:
                    if harvest == 'Corn': # if the farm block has corn
                        print('\n' + "Corn has been harvested. 30 corn had been added to your inventory")
                        print('------------------------------------------')
                        Inventory['Corn'] += 30 # adds 30 corn in the inventory
                        farm_layout[int(harvest_choice)] = 'Empty' # empties the farm block
                        farm_layout_1[int(harvest_choice)] = 'Empty'
                        harvest_m['Corn'] += 1 # for the harvest mission
                    elif harvest == 'Pumpkin': # if the farm block has pumpkin
                        if farm_layout[int(harvest_choice)+1][0] == 'Pumpkin': # checks if the succeeding block is also pumpkin
                            print('\n' + "Pumpkin has been harvested. 1 pumpkin had been added to your inventory")
                            print('------------------------------------------')
                            farm_layout[int(harvest_choice)] = 'Empty' # empties the chosen block
                            farm_layout_1[int(harvest_choice)] = 'Empty'
                            farm_layout[int(harvest_choice)+1] = 'Empty' # empties the succeeding block
                            farm_layout_1[int(harvest_choice)+1] = 'Empty'
                            Inventory['Pumpkin'] += 1 # adds 1 pumpkin in the inventory
                            harvest_m['Pumpkin'] += 1 # for the harvest mission
                        elif farm_layout[int(harvest_choice)-1][0] == 'Pumpkin': # checks if the preceding block is also pumpkin
                            print('\n' + "Pumpkin has been harvested. 1 pumpkin had been added to your inventory")
                            print('------------------------------------------')
                            farm_layout[int(harvest_choice)] = 'Empty' # empties the chosen block
                            farm_layout_1[int(harvest_choice)] = 'Empty'
                            farm_layout[int(harvest_choice)-1] = 'Empty' # empties the preceding block
                            farm_layout_1[int(harvest_choice)-1] = 'Empty'
                            Inventory['Pumpkin'] += 1 # adds 1 pumpkin in the inventory
                            harvest_m['Pumpkin'] += 1 # for the harvest mission
                        else:
                            print("Invalid farm block input.") # if neither of the blocks have pumpkin
                            print("--------------------------")
                    elif harvest == 'Eggs': # if the farm block has eggs
                        print('\n' + "Eggs have been harvested. 6 eggs had been added to your inventory")
                        print('------------------------------------------')
                        Inventory['Eggs'] += 6 # adds 6 eggs in the inventory
                        farm_layout[int(harvest_choice)] = 'Empty' # empties the chosen block
                        farm_layout_1[int(harvest_choice)] = 'Empty'
                        harvest_m['Eggs'] += 1 # for the harvest mission
                    elif harvest == 'Milk': # if the farm block has milk
                        print('\n' + "Milk has been harvested. 10 milks had been added to your inventory")
                        print('------------------------------------------')
                        Inventory['Milk'] += 10 # adds 10 milk in the inventory
                        farm_layout[int(harvest_choice)] = 'Empty' # empties the chosen block
                        farm_layout_1[int(harvest_choice)] = 'Empty'
                        harvest_m['Milk'] += 1 # for the harvest mission
            else:
                print('\n' + f"Farm block {harvest_choice} is empty. Choose another.") # if the farm block is empty
                print('------------------------------------------')
        elif farmlot_choice == '0': # returning to main menu
            break
        else:
            print("Invalid Input")
            print('---------------')
    save_inven(Inventory)
    save_farm(farm_layout)
    save_dfarm(farm_layout_1)
    save_harvestm(harvest_m)

# function for the item shop
def itemshop():
    wallet = ID.get('Wallet') # gets the value of the wallet
    wallet = int(wallet)
    if int(wallet) == 0: # if the value of wallet is zero, it returns to main menu
        print('\n' + "====================== ITEM SHOP ======================")
        print('\n' + f"Insufficient fund. You only have a balance of Php {int(wallet)}.")
        print("Returning to Main Menu.")
        print("-----------------------------------------------------------")
    else:
        print('\n' + "====================== ITEM SHOP ======================")
        print(f"Your wallet is: {str(wallet)}" + '\n')
        print("[1] Buy Farm Lot         | 10 Farm Blocks    @ 5,000.00")
        print("[2] Buy Maize            | Package (6 Seeds) @ 80.00")
        print("[3] Buy Pumpkin Seeds    | 1 Seed            @ 12.00")
        print("[4] Buy Cow              | 1 Cow             @ 20,000.00")
        print("[5] Buy Chicken          | 1 Chicken         @ 1,000.00")
        print("[0] Return to Main Menu") 
        while int(wallet)>0: # continuous choice as long as wallet != 0
            buy_item = input('\n' + "Enter item: ")
            if buy_item == '1' and int(wallet) < 5000: # if the user chooses farm lot but has insufficient funds
                print("-----------------------------------------------------------")
                print(f"Insufficient fund. You only have a balance of Php {int(wallet)}")
                print("-----------------------------------------------------------")
            elif buy_item == '2' and int(wallet) < 80: # if the user chooses maize but has insufficient funds
                print("-----------------------------------------------------------")
                print(f"Insufficient fund. You only have a balance of Php {int(wallet)}")
                print("-----------------------------------------------------------")
            elif buy_item == '3' and int(wallet) < 12: # if the user chooses pumpkin seeds but has insufficient funds
                print("-----------------------------------------------------------")
                print(f"Insufficient fund. You only have a balance of Php {int(wallet)}")
                print("-----------------------------------------------------------")
            elif buy_item == '4' and int(wallet) < 20000: # if the user chooses cow but has insufficient funds
                print("-----------------------------------------------------------")
                print(f"Insufficient fund. You only have a balance of Php {int(wallet)}")
                print("-----------------------------------------------------------")
            elif buy_item == '5' and int(wallet) < 1000: # if the user chooses chicken but has insufficient funds
                print("-----------------------------------------------------------")
                print(f"Insufficient fund. You only have a balance of Php {int(wallet)}")
                print("-----------------------------------------------------------")
            elif buy_item == '1': # if the user chooses farm lot
                wallet -= 5000
                Inventory['Farm Blocks'] += 10 # adds 10 farm blocks to the inventory
                buy_m['Farm Blocks'] += 1 # for the buy mission
                print("-----------------------------------------------------------")
                print("You bought 10 Farm Blocks")
                print(f"You have a balance of Php {wallet} left")
                print("-----------------------------------------------------------")
            elif buy_item == '2': # if the user chooses maize
                wallet -= 80
                Inventory['Maize'] += 6 # adds 6 maize to the inventory
                buy_m['Maize'] += 1 # for the buy mission
                print("-----------------------------------------------------------")
                print("You bought a package of maize (6 seeds)")
                print(f"You have a balance of Php {wallet} left")
                print("-----------------------------------------------------------")
            elif buy_item == '3': # if the user chooses pumpkin seeds
                wallet -= 12
                Inventory['Pumpkin Seeds'] += 1 # adds 1 pumpkin seed to the inventory
                buy_m['Pumpkin Seeds'] += 1 # for the buy mission
                print("-----------------------------------------------------------")
                print("You bought 1 pumpkin seed")
                print(f"You have a balance of Php {wallet} left")
                print("-----------------------------------------------------------")
            elif buy_item == '4': # if the user chooses cow
                wallet -= 20000
                Inventory['Cow'] += 1 # adds 1 cow to the inventory
                buy_m['Cow'] += 1 # for the buy mission
                print("-----------------------------------------------------------")
                print("You bought 1 cow")
                print(f"You have a balance of Php {wallet} left")
                print("-----------------------------------------------------------")
            elif buy_item == '5': # if the user chooses chicken
                wallet -= 1000
                Inventory['Chicken'] += 1 # adds 1 chicken to the inventory
                buy_m['Chicken'] += 1 # for the buy mission
                print("-----------------------------------------------------------")
                print("You bought 1 chicken")
                print(f"You have a balance of Php {wallet} left")
                print("-----------------------------------------------------------")
            elif buy_item == 'iluvcmsc12':
                Inventory['Maize'] += 6
                Inventory['Pumpkin Seeds'] += 1
                Inventory['Chicken'] += 1
                Inventory['Cow'] += 1
                print('\n' + "-----------------------------------------------------------")
                print("Code activated.")
                print("Congratulations! 6 maize, 1 pumpkin seed, 1 chicken, and 1 cow has been added to your inventory.")
                print("-----------------------------------------------------------")
            elif buy_item == '0': # if the user chooses to return to main menu
                print('\n' + "-----------------------------------------------------------")
                print(f"You have a current balance of Php {wallet}")
                print("-----------------------------------------------------------")
                print('\n'+ "Items in your inventory:") # prints the inventory
                for k,v in Inventory.items():
                    print(f"• {k}: {str(v)}")
                break
            else: # if invalid input
                print("-----------------------------------------------------------")
                print("Invalid input")
                print("-----------------------------------------------------------")
    ID['Wallet'] = wallet # updates the wallet
    save_wallet(ID)
    save_inven(Inventory)
    save_buym(buy_m)
    return wallet

# function for the inventory of items bought and items sold
def inventory():
    # checks if the inventory is empty
    if Inventory['Maize'] == 0 and Inventory['Pumpkin Seeds'] == 0 and Inventory['Chicken'] == 0 and Inventory['Cow'] == 0 and Inventory['Corn'] == 0 and Inventory['Pumpkin'] == 0 and Inventory['Milk'] == 0 and Inventory['Eggs'] == 0:
        print('\n' + "==================== INVENTORY ====================")
        print("No items available in your inventory.")
        print('-------------------------------------')
    else: # if the inventory has items
        print('\n' + "==================== INVENTORY ====================" + '\n')
        print("Items in your inventory:") # prints the items in the inventory
        for k,v in Inventory.items(): 
            print(f"• {k} : {str(v)}")
        print('\n' + "Items sold:") # prints the items sold
        for k,v in Sell.items():
            print(f"• {k} : {str(v)}")

# function for option four of the main menu
def option_four(): 
    # checks if the user has seeds or livestocks
    if Inventory['Farm Blocks'] == 0 and Inventory['Maize'] == 0 and Inventory['Pumpkin Seeds'] == 0 and Inventory['Chicken'] == 0 and Inventory['Cow'] == 0:
        print('\n' + "========== PLANT SEEDS OR TEND LIVESTOCKS ==========")
        print("No seeds and livestocks available.")
        print("-----------------------------------")
    else:
        while True:
            print('\n' + "========== PLANT SEEDS OR TEND LIVESTOCKS ==========")
            print("[1] Plant Seeds")
            print("[2] Tend Livestocks")
            print("[0] Return to Main Menu" + '\n')
            plant_care = input("Enter choice: ")
            if plant_care == '1': # if the user wishes to plant seeds
                plantseeds()
            elif plant_care == '2': # if the user wishes to tend livestocks
                tendlivestocks()
            elif plant_care == '0': # if the user wishes to return to main menu
                break
            else:
                print("Invalid input")
                print("--------------------------------")

# function for planting seeds
def plantseeds(): 
    # checks if the user has both maize and pumpkin seeds in the inventory
    if Inventory['Maize'] == 0 and Inventory['Pumpkin Seeds'] == 0:
            print('\n' + "No Available Seeds")
            print("--------------------------------")
    else:
        # prints the available seeds
        print('\n' + "=========== List of Available Seeds ===========")
        print(f"[1] Maize:          {Inventory['Maize']}")
        print(f"[2] Pumpkin Seeds:  {Inventory['Pumpkin Seeds']}")
        print("[0] Return" + '\n')
        plant = input("Which seeds would you plant? ")
        if plant == '1': # if the user wishes to plant maize
            if Inventory['Maize'] == 0: # checks if the user has maize in the inventory
                print("No maize available.")
                print("--------------------------------")
            else:
                maize_now = datetime.today() # current time or time of planting
                maize_harvest_time = maize_now + timedelta(seconds=30) # time of harvest
                where_block = input("Enter farm block: ")
                if int(where_block) > Inventory['Farm Blocks']: # checks if the chosen block is available
                    print(f"Invalid input. Farm Block {int(where_block)} is not available.")
                    print("----------------------------------------------------")
                else:
                    if farm_layout[int(where_block)] == 'Empty': # checks if the chosen block is empty or not
                        # appends the name, icon, and time of crop in <str>
                        farm_layout[int(where_block)] = ['Corn', '@', str(maize_now), str(maize_harvest_time)]
                        farm_layout_1[int(where_block)] = [maize_now, maize_harvest_time] # time in datetime.datetime format
                        Inventory['Maize'] -= 1 # subtracts 1 maize from the inventory
                        plant_m['Maize'] += 1 # for the plant mission
                        print('\n' + f"Maize planted in Farm Block {where_block}! {Inventory['Maize']} seed/s left.")
                        print("----------------------------------------------------")
                    else:
                        print('\n' + f"Farm block {where_block} is currently unavailable. Choose another.")
                        print("----------------------------------------------------")
                        plantseeds() # iterates if the chosen block is unavailable
        elif plant == '2': # if the user wishes to plant pumpkin seeds
            if Inventory['Pumpkin Seeds'] == 0: # checks if the user has pumpkin seeds in the inventory
                print("No pumpkin seeds available.")
                print("--------------------------------")
            else:
                pumpkin_now = datetime.today() # current time or time of planting
                pumpkin_harvest_time = pumpkin_now + timedelta(seconds=60) # time of harvest
                print("Planting pumpkin requires 2 farm blocks")
                where_block = int(input("Enter the starting farm block: "))
                where_block_2 = int(where_block) + 1
                if int(where_block) and int(where_block_2) > Inventory['Farm Blocks']: # checks if the chosen blocks are available
                    print(f"Invalid input. Farm Block {where_block} still not available.")
                    print("----------------------------------------------------")
                else:
                    if farm_layout[int(where_block)] == 'Empty' and farm_layout[int(where_block_2)] == 'Empty': # checks if the chosen block and succeding blocks are empty
                        # appends the name, icon, and time of crop in <str>
                        farm_layout[int(where_block)] = ['Pumpkin', 'o', str(pumpkin_now), str(pumpkin_harvest_time)]
                        farm_layout[int(where_block_2)] = ['Pumpkin', 'o', pumpkin_now, pumpkin_harvest_time]
                        # appends the time in datetime.datetime format
                        farm_layout_1[int(where_block)] = [pumpkin_now, pumpkin_harvest_time]
                        farm_layout_1[int(where_block_2)] = [pumpkin_now, pumpkin_harvest_time]
                        Inventory['Pumpkin Seeds'] -= 1 # subtracts 1 pumpkin seed from the inventory
                        plant_m['Pumpkin Seeds'] += 1 # for the plant mission
                        print('\n' + f"Pumpkin seeds planted in Farm Blocks {where_block} and {where_block_2}! {Inventory['Pumpkin Seeds']} seed/s left.")
                        print("----------------------------------------------------")
                    else:
                        print('\n' + f"Either farm block {where_block} or farm block {where_block_2} is currently unavailable. Choose another.")
                        print("----------------------------------------------------")
                        plantseeds() # iterates if the chosen blocks are unavailable
        elif plant != '0':
            print('\n' + "Invalid Input")
            print("---------------")
    save_inven(Inventory)
    save_farm(farm_layout)
    save_dfarm(farm_layout_1)
    save_plantm(plant_m)

# function for tending livestocks
def tendlivestocks():
    # checks if the user has both chicken and cow in the inventory
    if Inventory['Chicken'] == 0 and Inventory['Cow'] == 0:
            print('\n' + "No Available Livestocks")
            print("--------------------------------")
    else:
        # prints the available livestocks
        print('\n' + "=========== List of Available Livestocks ===========")
        print(f"[1] Chicken:    {Inventory['Chicken']}")
        print(f"[2] Cow:        {Inventory['Cow']}")  
        print("[0] Return" + '\n')     
        livestocks = input("Which livestock you want to tend? ")
        if livestocks == '1': # if the user wishes to tend chicken
            if Inventory['Chicken'] == 0: # checks if the user has chicken in the inventory
                print("No chickens available.")
                print("--------------------------------")
            else:
                chicken_now = datetime.today() # current time or time for tending
                chicken_harvest_time = chicken_now + timedelta(seconds=90) # time of harvest
                where_block = input("Enter farm block: ")
                if int(where_block) > Inventory['Farm Blocks']: # checks if the chosen block is available
                    print(f"Invalid input. Farm Block {where_block} is not available.")
                    print("----------------------------------------------------")
                else:
                    if farm_layout[int(where_block)] == 'Empty': #checks if the chosen block is empty or not
                        # appends the name, icons, and time of livestock in <str>
                        farm_layout[int(where_block)] = ['Eggs', 'o3o', str(chicken_now), str(chicken_harvest_time)]
                        farm_layout_1[int(where_block)] = [chicken_now, chicken_harvest_time] # time in datetime.datetime format
                        Inventory['Chicken'] -= 1 # subtracts 1 chicken from the inventory
                        plant_m['Chicken'] += 1 # for the plant mission
                        print('\n' + "Take good care of the chicken!")
                        print("----------------------------------------------------")
                    else:
                        print('\n' + "Farm block is currently unavailable. Choose another")
                        print("----------------------------------------------------")
                        tendlivestocks() # iterates if the chosen farm block is unavailable
        elif livestocks == '2': # if the user wishes to tend cow
            if Inventory['Cow'] == 0: # checks if the user has cow in the inventory
                print("No cows available.")
                print("--------------------------------")
            else:
                cow_now = datetime.today() # current time or time for tending
                cow_harvest_time = cow_now + timedelta(seconds=120) # time of harvest
                where_block = input("Enter farm block: ")
                if int(where_block) > Inventory['Farm Blocks']: # checks if the farm block is available
                    print(f"Invalid input. Farm Block {where_block} still not available.")
                    print("----------------------------------------------------")
                else:
                    if farm_layout[int(where_block)] == 'Empty': # checks if the chosen farm block is empty or not
                        # appends the name, icon, and time of livestock in <str>
                        farm_layout[int(where_block)] = ['Milk', 'o#o', str(cow_now), str(cow_harvest_time)]
                        farm_layout_1[int(where_block)] = [cow_now, cow_harvest_time] # time in datetime.datetime format
                        Inventory['Cow'] -= 1 # subtracts 1 cow from the inventory
                        plant_m['Cow'] += 1 # for the plant mission
                        print('\n' + "Take good care of the cow!")
                        print("----------------------------------------------------")
                    else:
                        print('\n' + "Farm block is currently unavailable. Choose another.")
                        print("-----------------------------------------------------")
                        tendlivestocks() # iterates if the chosen farm block is unavailable
        elif livestocks != '0':
            print('\n' + "Invalid Input")
            print("--------------")
    save_inven(Inventory)
    save_farm(farm_layout)
    save_dfarm(farm_layout_1)
    save_plantm(plant_m)

# function for selling items
def sell():
    # checks if the user has items in the inventory
    if Inventory['Farm Blocks'] == 0 and Inventory['Maize'] == 0 and Inventory['Pumpkin Seeds'] == 0 and Inventory['Chicken'] == 0 and Inventory['Cow'] == 0 and Inventory['Corn'] == 0 and Inventory['Pumpkin'] == 0 and Inventory['Milk'] == 0 and Inventory['Eggs'] == 0:
        print('\n' + "=============== SELL FARM PRODUCE ==============")
        print("No items available to sell.")
        print("--------------------------------------")
    else: # prints available items in the inventory
        print('\n' + "=============== SELL FARM PRODUCE ==============")
        print("-------- List of Available Items to Sell -------")
        print(f"[1] Farm Blocks:     {Inventory['Farm Blocks']}")
        print(f"[2] Maize:           {Inventory['Maize']}")
        print(f"[3] Pumpkin Seeds:   {Inventory['Pumpkin Seeds']}")
        print(f"[4] Chicken:         {Inventory['Chicken']}")
        print(f"[5] Cow:             {Inventory['Cow']}")
        print(f"[6] Corn:            {Inventory['Corn']}")
        print(f"[7] Pumpkin:         {Inventory['Pumpkin']}")
        print(f"[8] Eggs:            {Inventory['Eggs']}")
        print(f"[9] Milk:            {Inventory['Milk']}")
        print("[0] Return to Main Menu" + '\n')
        budget = ID['Wallet'] # gets the value of wallet
        while True: # continuous choice for selling items
            sell_choice = input("Enter choice: ")
            if sell_choice == '0': # if the user wishes to return to main menu
                break
            elif sell_choice == '1': # if the user wishes to sell a farm lot
                if Inventory['Farm Blocks'] == 0: # checks if farm lot is available
                    print("Not available.")
                    print("----------------------" + '\n')
                else:
                    budget += 4500 # adds to the wallet
                    Inventory['Farm Blocks'] -= 10 # subtracts 10 farm blocks
                    Sell['Farm Blocks'] += 10 # adds 10 farm blocks to sold items
                    print('-----------------------------------------------------')
                    print("Farm Blocks successfully sold! Available stock/s left: ", Inventory['Farm Blocks'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '2': # if the user wishes to sell maize
                if Inventory['Maize'] == 0: # checks if maize is available
                    print("No stock available.")
                    print("----------------------" + '\n')
                elif Inventory['Maize'] < 6: # checks if there is enough stock
                    print("Does not have enough stock.")
                    print("----------------------------" + '\n')
                else:
                    budget += 64 # adds to the wallet
                    Inventory['Maize'] -= 6 # subtracts 6 maize
                    Sell['Maize'] += 6 # adds 6 maize to sold items
                    print('-----------------------------------------------------')
                    print("Maize successfully sold! Available stock/s left: ", Inventory['Maize'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '3': # if the user wishes to sell pumpkin seeds
                if Inventory['Pumpkin Seeds'] == 0: # checks if pumpkin seeds are available
                    print("No stock available.")
                    print("----------------------" + '\n')
                else:
                    budget += 9.6 # adds to the wallet
                    Inventory['Pumpkin Seeds'] -= 1 # subtracts 1 pumpkin seed
                    Sell['Pumpkin Seeds'] += 1 # adds 1 pumpkin seed to sold item
                    print('-----------------------------------------------------')
                    print("Pumpkin Seeds successfully sold! Available stock/s left: ", Inventory['Pumpkin Seeds'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '4': # if the user wishes to sell chicken
                if Inventory['Chicken'] == 0: # checks if chicken is available
                    print("No stock available.")
                    print("----------------------" + '\n')
                else:
                    budget += 800 # adds to the wallet
                    Inventory['Chicken'] -= 1 # subtracts 1 chicken
                    Sell['Chicken'] += 1 # adds 1 chicken to the sold items
                    print('-----------------------------------------------------')
                    print("Chicken successfully sold! Available stock/s left: ", Inventory['Chicken'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '5': # if the user wishes to sell cow
                if Inventory['Cow'] == 0: # checks if cow is available
                    print("No stock available.")
                    print("----------------------" + '\n')
                else:
                    budget += 18000 # adds to the wallet
                    Inventory['Cow'] -= 1 # subtracts 1 cow
                    Sell['Cow'] += 1 # adds 1 cow to the sold items
                    print('-----------------------------------------------------')
                    print("Cow successfully sold! Available stock/s left: ", Inventory['Cow'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '6': # if the user wishes to sell corn
                if Inventory['Corn'] == 0: # checks if corn is available
                    print("No stock available.")
                    print("----------------------" + '\n')
                elif Inventory['Corn'] < 60: # checks if there is enough stock
                    print("Does not have enough stock.")
                    print("----------------------" + '\n')
                else:
                    budget += 400 # adds to the budget
                    Inventory['Corn'] -= 60 # subtracts 60 corn
                    Sell['Corn'] += 60 # adds 60 corn to sold items
                    print('-----------------------------------------------------')
                    print("Corn successfully sold! Available stock/s left: ", Inventory['Corn'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '7': # if the user wishes to sell pumpkin
                if Inventory['Pumpkin'] == 0: # checks if pumpkin is available
                    print("No stock available.")
                    print("----------------------" + '\n')
                else:
                    budget += 150 # adds to the wallet
                    Inventory['Pumpkin'] -= 1 # subtracts 1 pumpkin
                    Sell['Pumpkin'] += 1 # adds 1 pumpkin to sold items
                    print('-----------------------------------------------------')
                    print("Pumpkin successfully sold! Available stock/s left: ", Inventory['Pumpkin'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '8': # if the user wishes to sell eggs
                if Inventory['Eggs'] == 0: # checks if eggs are available
                    print("No stock available.")
                    print("----------------------" + '\n')
                elif Inventory['Eggs'] < 12: # checks if there is enough stock
                    print("Does not have enough stock.")
                    print("----------------------" + '\n')
                else:
                    budget += 100 # adds to the wallet
                    Inventory['Eggs'] -= 12 # subtracts 12 eggs
                    Sell['Eggs'] += 12 # adds 12 eggs to sold items
                    print('-----------------------------------------------------')
                    print("Eggs successfully sold! Available stock/s left: ", Inventory['Eggs'])
                    print('-----------------------------------------------------' +'\n')
            elif sell_choice == '9': # if the user wishes to sell milk
                if Inventory['Milk'] == 0: # checks if milk is available
                    print("No stock available.")
                    print("----------------------" + '\n')
                else:
                    budget += 200 # adds to the wallet
                    Inventory['Milk'] -= 1 # subtracts 1 milk
                    Sell['Milk'] += 1 # adds 1 milk to sold items
                    print('-----------------------------------------------------')
                    print("Milk successfully sold! Available stock/s left: ", Inventory['Milk'])
                    print('-----------------------------------------------------' +'\n')
            else:
                print('Invalid input')
                print("----------------------" + '\n')
                
        ID['Wallet'] = budget # updates the value of the wallet
    save_wallet(ID)
    save_inven(Inventory)
    save_sell(Sell)

# function for all missions
def missions():
    print('\n' + "================== MISSIONS =================")
    print("[1] Plant and Tend Missions")
    print("[2] Harvest Missions")
    print("[3] Buy Missions")
    print("[0] Return to Main Menu" + '\n')
    missions_choice = input("Enter choice: ")
    if missions_choice == '1': #if the user wishes to view or do plant mission
        plant_mission()
    elif missions_choice == '2': #if the user wishes to view or do harvest mission
        harvest_mission()
    elif missions_choice == '3': #if the user wishes to view or do buy mission
        buy_mission()
    elif missions_choice != '0':
        print('Invalid input')
        print("--------------")

# function for the plant mission
def plant_mission():
    print('\n' + "================ PLANT MISSIONS ===============")
    print("View progress on missions")
    print("[1] Plant Maize 15 times.")
    print("[2] Plant Pumpkin Seeds 10 times.")
    print("[3] Tend Chicken 5 times.")
    print("[4] Tend Cow 5 times.")
    print("[0] Return to Main Menu" + '\n')
    while True:
        plantm = input("Enter choice: ")
        if plantm == '1':
            if plant_m['Maize'] >= 15: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only planted {plant_m['Maize']} Maize. Plant {int(15 - plant_m['Maize'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif plantm == '2':
            if plant_m['Pumpkin Seeds'] >= 10: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only planted {plant_m['Pumpkin Seeds']} pumpkin seed/s. Plant {int(10 - plant_m['Pumpkin Seeds'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif plantm == '3':
            if plant_m['Chicken'] >= 5: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only tend {plant_m['Chicken']} chicken/s. Tend {int(5 - plant_m['Chicken'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif plantm == '4':
            if plant_m['Cow'] >= 5: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only tend {plant_m['Cow']} cow/s. Tend {int(5 - plant_m['Cow'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif plantm == '0':
            break
        else:
            print('Invalid input')
            print("--------------" + '\n')
    
        save_wallet(ID)

# function for the harvest mission
def harvest_mission():
    print('\n' + "================ HARVEST MISSIONS ===============")
    print("View progress on missions")
    print("[1] Harvest Corn 20 times.")
    print("[2] Harvest Pumpkin 15 times.")
    print("[3] Harvest Eggs 10 times.")
    print("[4] Harvest Milk 5 times.")
    print("[0] Return to Main Menu" + '\n')
    while True:
        harvestm = input("Enter choice: ")
        if harvestm == '1':
            if harvest_m['Corn'] >= 20: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only harvested {harvest_m['Corn']} times. Harvest {int(20 - harvest_m['Corn'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif harvestm == '2':
            if harvest_m['Pumpkin'] >= 15: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only harvested {harvest_m['Pumpkin']} times. Harvest {int(15 - harvest_m['Pumpkin'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif harvestm == '3':
            if harvest_m['Eggs'] >= 10: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only harvested {harvest_m['Eggs']} times. Harvest {int(10 - harvest_m['Eggs'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif harvestm == '4':
            if harvest_m['Milk'] >= 5: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You have only harvested {harvest_m['Milk']} times. Harvest {int(5 - harvest_m['Milk'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif harvestm == '0':
            break
        else:
            print('Invalid input')
            print("--------------" + '\n')
    
        save_wallet(ID)

# function for the buy mission
def buy_mission():
    print('\n' + "================ BUY MISSIONS ===============")
    print("View progress on missions")
    print("[1] Buy Farm Lot 5 times.")
    print("[2] Buy Maize 10 times.")
    print("[3] Buy Pumpkin Seeds 7 times.")
    print("[4] Buy Chicken 5 times.")
    print("[5] Buy Cow 5 times.")
    print("[0] Return to Main Menu" + '\n')
    while True:
        buym = input("Enter choice: ")
        if buym == '1':
            if buy_m['Farm Blocks'] >= 5: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------")
                ID['Wallet'] += 500
            else:
                print('\n' + f"You bought {buy_m['Farm Blocks']} farm block/s. Buy {int(5 - buy_m['Farm Blocks'])} more to complete.")
                print("-------------------------------------------------")
        elif buym == '2':
            if buy_m['Maize'] >= 10: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------")
                ID['Wallet'] += 500
            else:
                print('\n' + f"You bought {buy_m['Maize']} maize. Buy {int(10 - buy_m['Maize'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif buym == '3':
            if buy_m['Pumpkin Seeds'] >= 7: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You bought {buy_m['Pumpkin Seeds']} pumpkin seed/s. Buy {int(7 - buy_m['Pumpkin Seeds'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif buym == '4':
            if buy_m['Chicken'] >= 5: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You bought {buy_m['Chicken']} chicken/s. Buy {int(5 - buy_m['Chicken'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif buym == '5':
            if buy_m['Cow'] >= 5: # checks if the mission is complete
                print('\n' + "Mission Complete!")
                print("Php 500 has been added to your wallet.")
                print("--------------------------" + '\n')
                ID['Wallet'] += 500
            else:
                print('\n' + f"You bought {buy_m['Cow']} cow/s. Buy {int(5 - buy_m['Cow'])} more to complete.")
                print("-------------------------------------------------" + '\n')
        elif buym == '0':
            break
        else:
            print('Invalid input')
            print("--------------" + '\n')
    
        save_wallet(ID)

# function for exit message
def exit():
    print('\n' + "Thank you for playing Farm2Market!")
    print("I hope you had an amazing experience. Make sure to comeback 'cause your farm is waiting for you." +'\n')

# start of the program
welcomemsg()
ID = load_wallet(ID) # loads the wallet
Inventory = load_inven(Inventory) # loads the inventory
Sell = load_sell(Sell) # loads the sold items
farm_layout = load_farm(farm_layout) # loads the farm lot
farm_layout_1 = load_dfarm(farm_layout_1) # loads the date and time in farm lot
plant_m = load_plantm(plant_m)
harvest_m = load_harvestm(harvest_m)
buy_m = load_buym(buy_m)
inputID() # inputs ID
sign_in()
while True:
    mainmenu()
    menu_choice = input("Enter choice: ") # menu choice for the user
    if menu_choice == '1': # calls the farmlot function
        farmlot()
    elif menu_choice == '2': # calls the itemshop function
        itemshop()
    elif menu_choice == '3': # calls the inventory function
        inventory()
    elif menu_choice == '4': # calls the function for this choice [planting seeds and tending livestocks]
        option_four()
    elif menu_choice == '5': # calls the sell function
        sell()
    elif menu_choice == 'slaysomuch': # hidden code
        ID['Wallet'] += 5000
        print('\n' + "-----------------------------")
        print('Code activated.')
        print('Congratulations! Php 5,000 has been added to your wallet')
        print("------------------------------")
        save_wallet(ID)
    elif menu_choice == 'dsurv': # hidden code
        ID['Wallet'] -= 5000
        print('\n' + "-----------------------------")
        print('Code activated.')
        print('Awww! I am sorry! Php 5,000 has been deducted from your wallet')
        print("------------------------------")
        save_wallet(ID)
    elif menu_choice == '6':
        missions()
    elif menu_choice == '0': # if the user wishes to exit
        bye = input("[1] Yes  [0] No  |   Are you sure you want to exit? " )
        if bye == '1':
            exit() # calls the exit message function
            break
        elif bye != '0': # returns to main menu
            print("Invalid input")
            print('---------------')
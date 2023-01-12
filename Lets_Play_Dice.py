from time import sleep
import random

""" We will be playing dice, where two players will start with 100 dollars and a virttual dice will be rolled.
who ever gets the highest number wins the money they bet. 

1. Two players total with one player being the bet maker, meaning that whatever he bets, other person gotta match it.
If the bet is too high then the non bet player can roll a dice and if the non bet player gets the highest, he/she has too 
pick a number lower than the initial bet.  

2. The bet maker switches every turn and each person can contest the bet ONCE if they think the bet is too high.

3. Whoever loses all their money first, loses, DUHHH"""


print("Welcome to LETS PLAY DICEEE. this is not a kid friendly game and you might go broke. SO play with caution!\n")

print("We have two players, and both will start with 100 dollars \n")

# Each player enters their name
player_one = input("Player one, what is your name: \n")

player_two = input("Player two, what is your name: \n")

print('Welcome to the game {} and {}'.format(player_one,player_two))
 
# setting the variables for how much money they have; total turns played; and the total pot  
P1_money = 100
P2_money = 100
total_turns = 0
total_pot = 0

# Creating dictionary for each player 
User_one = {"player": player_one, "money": P1_money}
User_two = {"player":player_two, "money": P2_money}

# Keeps in check who the bet master is, since it alternates
def Bet_maker(turns):
    while True:
        if (User_one["money"] == 0) and (User_two["money"] > 0):
            print(f'Game over: {User_one["player"]} went bankrupt!')
            break
        elif (User_one["money"] > 0) and (User_two["money"] == 0):
            print(f'Game over: {User_two["player"]} went bankrupt!')
            break
        else:
            # This will change the bet maker
            if turns % 2 == 0:
                turns = turns + 1
                bet_Master_one(User_one)

            else:
                turns = turns + 1
                bet_Master_two(User_two)

# Bet master needs to place his bets, and this is for user one when he is bet master
def bet_Master_one(U1):

    This_true = True

    # The bet master will place his bets, but it has to be less than he has
    while This_true:
        
        print(f'You are the bet master {User_one["player"]}, and you have {User_one["money"]}')
        print("How much would you like to bet?")
        

        # Enters the amount 
        gambling_amount = int(input())
        
        
        sleep(3)
        # Will check if the amount he entered is valid
        if ((gambling_amount <= User_one["money"]) and (gambling_amount > 0)):
            print("Each person will put that amount of money in the pot.\n")
            This_true = False
        else:
            print("Pick an amount you have: ")
            

    # Once the bet has been accepted, than the money will be taken from each account and placed in the pot.
    # If both people have enough money then it will take the gambling amount 
    if gambling_amount <= User_one["money"] and gambling_amount <= User_two["money"]:
        total_pot = gambling_amount * 2
        
        User_one["money"] = User_one["money"] - gambling_amount
        User_two["money"] = User_two["money"] - gambling_amount
        
    # If the non bet master has less than the gambling amount then it will just withdraw whatever they have left.    
    elif gambling_amount >= User_one["money"] and gambling_amount <= User_two["money"]:
        total_pot = gambling_amount + User_one["money"]
        
        User_one["money"] = User_one["money"] - User_one["money"]
        User_two["money"] = User_two["money"] - gambling_amount
        
        
        
    elif gambling_amount <= User_one["money"] and gambling_amount >= User_two["money"]:
        total_pot = gambling_amount + User_two["money"]
        
        User_one["money"] = User_one["money"] - gambling_amount
        User_two["money"] = User_two["money"] - User_two["money"]
        
    print(f'The total pot contains: ${total_pot}')

    sleep(2)
    # Player one will roll the dice first 
    print(f'The dice will be rolled and who ever gets the highest number wins!\n')
    print(f'{User_one["player"]}, you roll the dice first. \n')

    # The random library will pick a number from 1-6
    first_Number = random.randint(1,6)

    print(f'{User_one["player"]}, rolled a {first_Number}')
    
    sleep(2)
    print(f'{User_two["player"]}, you have the dice.\n')

    # Player two will roll the dice and the random op will pick a number from 1-6
    second_Number = random.randint(1,6)

    print(f'{User_two["player"]}, rolled a {second_Number} \n')

    sleep(3)
    # If else loop will decide who gets the money, if it ends in a draw then they both lose the pot
    if (first_Number > second_Number):
        print(f'{User_one["player"]} rolled higher and wins the total pot!\n')
        User_one["money"] = User_one["money"] + total_pot
    elif (first_Number < second_Number):
        print(f'{User_two["player"]} rolled higher and wins the total pot!\n')
        User_two["money"] = User_two["money"] + total_pot
    else:
        print("It is a draw, and the players will be refunded the money.\n")
        User_one["money"] = User_one["money"] + gambling_amount
        User_two["money"] = User_two["money"] + gambling_amount

    print(f'{User_one["player"]} has ${User_one["money"]} left. \n')
    print(f'{User_two["player"]} has ${User_two["money"]} left.')
    
    
def bet_Master_two(U2):

    This_true = True

    # The bet master will place his bets, but it has to be less than he has
    while This_true:
        
        print(f'You are the bet master {User_two["player"]}, and you have {User_two["money"]}')
        print("How much would you like to bet?")

        # Enters the amount 
        gambling_amount = int(input())

        sleep(2)
        # Will check if the amount he entered is valid
        if ((gambling_amount <= User_two["money"]) and (gambling_amount > 0)):
            print("Each person will put that amount of money in the pot.\n")
            This_true = False
        else:
            print("Pick an amount you have: ")
            

    # Once the bet has been accepted, than the money will be taken from each account and placed in the pot.
    # If both people have enough money then it will take the gambling amount 
    if gambling_amount <= User_one["money"] and gambling_amount <= User_two["money"]:
        total_pot = gambling_amount * 2
        
        User_one["money"] = User_one["money"] - gambling_amount
        User_two["money"] = User_two["money"] - gambling_amount
        
    # If the non bet master has less than the gambling amount then it will just withdraw whatever they have left.    
    elif gambling_amount >= User_one["money"] and gambling_amount <= User_two["money"]:
        total_pot = gambling_amount + User_one["money"]
        
        User_one["money"] = User_one["money"] - User_one["money"]
        User_two["money"] = User_two["money"] - gambling_amount
        
        
        
    elif gambling_amount <= User_one["money"] and gambling_amount >= User_two["money"]:
        total_pot = gambling_amount + User_two["money"]
        
        User_one["money"] = User_one["money"] - gambling_amount
        User_two["money"] = User_two["money"] - User_two["money"]
        
    print(f'The total pot contains: ${total_pot}')

    sleep(2)
    # Player two will roll the dice first 
    print(f'The dice will be rolled and who ever gets the highest number wins!\n')
    print(f'{User_two["player"]}, you roll the dice first.')

    # The random library will pick a number from 1-6
    first_Number = random.randint(1,6)

    print(f'{User_two["player"]} rolled a {first_Number} \n')

    sleep(2)
    print(f'{User_one["player"]} you have the dice.')
    # Player one will roll the dice and the random op will pick a number from 1-6
    second_Number = random.randint(1,6)

    print(f'{User_one["player"]} rolled a {second_Number} \n')

    sleep(3)
    # If else loop will decide who gets the money, if it ends in a draw then both players will be refunded the money
    if (first_Number > second_Number):
        print(f'{User_two["player"]} rolled higher and wins the total pot!\n')
        User_two["money"] = User_two["money"] + total_pot
        
    elif (first_Number < second_Number):
        print(f'{User_one["player"]} rolled higher and wins the total pot!\n')
        User_one["money"] = User_one["money"] + total_pot
        
    else:
        print("It is a draw, and the players will be refunded the money.\n")
        User_one["money"] = User_one["money"] + gambling_amount
        User_two["money"] = User_two["money"] + gambling_amount

    print(f'{User_one["player"]} has ${User_one["money"]} left. \n')
    print(f'{User_two["player"]} has ${User_two["money"]} left.')
    
    Bet_maker(total_turns)


test = Bet_maker(total_turns)


    






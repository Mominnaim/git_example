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
print("Player one, what is your name: \n")
player_one = input()

print("Player two, what is your name: \n")
player_two = input()

print('Greetings {} and {}'.format(player_one,player_two))
 
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
    # This will change the bet maker
    if turns % 2 == 0:
        return bet_Master(User_one)

    else:
        return User_two["player"]

# Bet master needs to place his bets, and this is for user one when he is bet master
def bet_Master(U1):

    This_true = True

    # The bet master will place his bets, but it has to be less than he has
    while This_true:
        print("{} is the bet master. pick how much you would like to bet.\n".format(User_one["player"]))
        print("{} has {} left!.".format(User_one["player"],User_one["money"]))

        # Enters the amount 
        gambling_amount = int(input())

        # Will check if the amount he entered is valid
        if ((gambling_amount < User_one["money"]) and (gambling_amount > 0)):
            print("Each person will put that amount of money in the pot.\n")
            This_true = False
        else:
            print("Pick an amount you have: ")
            

    # Once the bet has been accepted, than the money will be taken from each account and placed in the pot.
    User_one["money"] = User_one["money"] - gambling_amount
    User_two["money"] = User_two["money"] - gambling_amount

    total_pot = gambling_amount * 2

    print(f'The dice will be rolled and who ever gets the highest number wins!\n')
    print(f'{User_one["player"]}, you roll the dice first. \n')

    first_Number = random.randint(1,6)

    print(f'{User_one["player"]}, rolled a {first_Number} \n')

    print(f'{User_two["player"]}, you have the dice.')

    second_Number = random.randint(1,6)

    print(f'{User_two["player"]}, rolled a {second_Number} \n')

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

test = Bet_maker(total_turns)

print(total_pot)
print(User_one["money"])
print(User_two["money"])




"""def main(Player_one,Player_two):
    if Bet_maker(total_turns) == User_one["player"]:
        print(f'{User_one["player"]} is the bet master')
        
    elif Bet_maker(total_turns) == User_two["player"]:
        print(f'{User_two["player"]}is the bet master')
            
main(User_one,User_two)
 """ 







backstory = """ So since I have already learned the if else
I will just use what I know and make something complex"""

print(backstory + "\n")

print("pick a number from  1 to 3")
first_input = input()

print("pick a variant from 1-2")
second_input = input()

def variant(v):
    if v == 1:
        print("you are the stronger variant")
    elif v == 2:
        print("you are the weaker variant")



if first_input == 1:
    print("you are a tiger")
    who = variant(second_input)
elif first_input == 2:
    print("you are a monkey")
    who = variant(second_input)
elif first_input == 3:
    print("you are a human")
    who = variant(second_input)
else:
    print("you are poop")



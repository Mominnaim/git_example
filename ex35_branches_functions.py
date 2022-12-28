from sys import exit

# This will be the starting room and from here doors will open up.

def black():
    print("You have arrived in the black room")
    print("The answer to this question will lead you to the next door so pick wisely.")
    print("There is a train coming and has a blue path and a red path.")
    print("On the blue path there is a 5 people attached to the trail.")
    print("On the red path there is a pregnant lady attached to the trail.")
    print("You have the lever to decide who will live and who will die.")

    print("What path are you picking for the train to through")
    pick_path = input()

    if pick_path.lower() == "red":
        red()
    elif pick_path.lower() == "blue":
        blue()
    else:
        exit(0)

#Kill the pregnant lady and now your here, pick what test you would take, math or science   
def red():

    print("So you decided to kill the pregnant lady.")
    print("You should wonder why you chose that not the blue path")

    print("Next question: If you had to take one test to save your friends life which test would it be")
    print("you have two options -> MATH or SCIENCE")

    pick_test = input(" > ")

    if pick_test.lower() == "math":
        MATH()
    elif pick_test.lower() == "science":
        SCIENCE()
    else:
        exit(0)

# Kill the 5 people and now your here, pick your fav number 1 or 2, or just breeak the rules
def blue():


    print("You decided to kill 5 people, how do you feel, murdered!!")
    print("Just kidding, this is just an exercise")
    print("But heres your next question -> pick 1 or 2")

    pick_Number = input()

    if pick_Number.lower() == "1":
        print("Your favorite number is 1.")
    elif pick_Number.lower() == "2":
        print("Your favorite number is 2.")
    else:
        print("BREAK THE RULES MAYNEE")
        exit(0)

#Take the math test, Good job!
def MATH():
    print("You love number dont you!!")

#Take the science test, Good job!
def SCIENCE():  
    print("You love concepts dont you!!")


black()







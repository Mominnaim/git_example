import sys

print("This exercise file will be here to show what I have learned \n")

what_have_we_learned = """ Things I have learned is 
\t-multiline strings
\t-Functions and def
\t-Argv and unpacking
\t-pass in variables through to a printLine
"""

print(what_have_we_learned, "\n")

print("Now we will go over things like argv and de/functions \n")



def random(*argv):
    person, place, thing = argv

    print(f"Since we are human, we live in {place}")
    print(f"Since we are human, we are {person}")
    print(f"Since we are human, we have {thing}")

random("naim","Texas","money")







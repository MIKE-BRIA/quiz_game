import random

sides=int(input("How many sides? "))
playgame = "yes"

def roll(sides):
    print("You rolled", random.randint(1,sides))
    
while playgame == "yes":
    roll(sides)
    playgame = input("roll again")
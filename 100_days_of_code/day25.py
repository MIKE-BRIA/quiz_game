import random

def rolldice(sides):
    results=random.randint(1,sides)
    return results
def roll_6_and_8():
    roll_6=rolldice(6)
    roll_8=rolldice(8)
    health=roll_6 * roll_8
    return health


print("A CHARACTER GENERATOR STATS")
character="yes"
character=character.lower()

while character=="yes":
    cha=input("What's the name of your character? ")
    health= str(roll_6_and_8())
    print("Their health is", health,"hp")
    character=input("Do you want to continue")
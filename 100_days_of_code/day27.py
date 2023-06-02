import os, random, time

print("CHARACTER BUILDER ")

def char():
    print("Name your Legend")
    leg=input("Name: ")
    print("Character type(Human, Elf, Wizard, Orc)")
    cha=input("Character type: ")
    print(leg)
    
def dice(sides):
    results=random.randint(1,sides)
    return results

def health():
    status=((dice(6) * dice(12))/2)+12
    return status

def strength():
    strong=((dice(6) * dice(12))/2)+12
    return strong

while True:
    char()
    print("Health:", health())
    print("Strength:", strength())
    print()
    print("Am the king of all worldly kings am the most powerful man on planet earth")
    print()
    play=input("Do you want to do this again? ")
    play=play.lower
    if play == "No":
        break
    
    time.sleep(1)
    os.system("clear")
    
        
    

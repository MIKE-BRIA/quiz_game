import os, time, random

print("CHARACTER BUILDER ")

def dice(sides):
    results=random.randint(1,sides)
    return results

def health():
    status=((dice(6) * dice(12))/2)+12
    return status

def strength():
    strong=((dice(6) * dice(12))/2)+12
    return strong

print("BATTLE TIME")
print()
c1name=input("Name your legend: ")
c1type=input("Character type (Human, Elf, Wizard, Orc): ")
print()
print(c1name)
c1health=health()
c1strength=strength()
print("Health:", c1health)
print("Strength:", c1strength)
print()
print("Who is our enermy for today")
print()

c2name=input("Name your Legend: ")
c2type=input("Character type(Human, Elf, Wizard, Orc): ")
print()
print(c2name)
c2health=health()
c2strength=strength()
print("Health:", c2health)
print("Strength:", c2strength)
print()

round = 1
winner= None

while True:
  time.sleep(1)
  os.system("clear")
  print("BATTLE TIME")
  print()
  print("The battle begins!")

  c1dice=dice(6)
  c2dice=dice(6)

  difference=abs(c1strength-c2strength) + 1

  if c1dice > c2dice:
    c2health -= difference
    if round ==1:
      print(c2name, "wins round", round)
    else:
      print(c2name, "wins round", round)
  elif c2dice>c1dice:
    c1health-=difference
    if round==1:
      print(c2name, "wins the first blow")
    else:
      print(c2name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1name)
  print("Health:", c1health)
  print()
  print(c2name)
  print("Health", c2health)
  print()

  if c1health<=0:
    print(c1name, "has died")
    winner=c2name
    break
  elif c2health<=0:
    print(c2name, "has died")
    winner=c1name
    break
  else:
    print("And they are both standing for the next round")
    round+=1

time.sleep(1)
os.system("clear")
print('BATTLE TIME')
print()
print(winner, "has won in", round,"rounds")
    
      
import time,os

def color():
  if type =="water":
    return("\033[34m")
  if type=="fire":
    return("\033[31m")
  if type=="earth":
    return("\033[32m")
  if type=="pumpum":
    return("\033[35m")


while True:
  time.sleep(3)
  os.system("clear")
  print("MokeBeast - The Non-Copyright Generic Beast Battle Game")
  print()
  
  name=input("Input your beast's name: ").strip().lower()
  type=input("Input your beast's type: ").strip().lower()
  move=input("Input your beast's special move: ").strip().lower()
  hp=input("Input your best starting HP: ").strip().lower()
  mp=input("Input your beast's staring MP: ").strip().lower()

  game={"Name": name, "type": type, "Move": move, "HP": hp, "MP": mp}

  for key, values in game.items():
    print(f"{color()}{key} : {values}")
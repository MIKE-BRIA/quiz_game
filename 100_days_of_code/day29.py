def newprint(color,word):
  if color =="red":
    print("\033[31m", word,sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
newprint("red", "new program")
newprint("reset", " i can just call red('and')")
newprint("red", "it will print in red")
newprint("blue", "or even blue")
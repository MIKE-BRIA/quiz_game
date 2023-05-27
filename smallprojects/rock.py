from getpass import getpass as input

print("Player one")
p1=input("Choose between rock paper and scissors: ")
print("Player two")
p2=input('Choose between rock, paper and scissors: ')

if p1== "rock" :
  if p2 == "scissors":
    print("Player one won the game")
  elif p2 == "paper":
    print("Player two won the game")
  elif p2 == "rock":
    print("Both player one and two tied")
elif p1 == "paper" :
  if p2 == "rock":
    print("Player two won the game")
  elif p2 == "paper":
    print("Both player one and two tied")
  elif p2 == "scissors":
    print("Player two won the game")
elif p1 == "scissors":
  if p2 == "rock":
    print("Player two won the game")
  elif p2 =="paper":
    print("Player one won the game")
  elif p2 =="scissors":
    print("Both player one and two tied")
else:
  print("are you sure you placed the correct inputs")

from getpass import getpass as input

player1score=0
player2score=0

while True:
  print("Player one")
  p1=input("Choose between rock paper and scissors: ")
  print("Player two")
  p2=input('Choose between rock, paper and scissors: ')

  if p1== "rock" :
    if p2 == "scissors":
      print("Player one won the game")
      player1score+=1
    elif p2 == "paper":
      print("Player two won the game")
      player2score+=1
    elif p2 == "rock":
      print("Both player one and two tied")
  elif p1 == "paper" :
    if p2 == "rock":
      print("Player two won the game")
      player2score+=1
    elif p2 == "paper":
      print("Both player one and two tied")
    elif p2 == "scissors":
      print("Player two won the game")
      player2score+=1
  elif p1 == "scissors":
    if p2 == "rock":
      print("Player two won the game")
      player2score+=1
    elif p2 =="paper":
      print("Player one won the game")
      player1score+=1
    elif p2 =="scissors":
      print("Both player one and two tied")
  else:
    print("are you sure you placed the correct inputs")
    
    
  print("player one has",player1score,"points")
  print("player two has",player2score,"points")
    
  if player1score==5 or player2score==5:
    print("We welcome you next time for a better experience")
    exit()
  else:
    continue
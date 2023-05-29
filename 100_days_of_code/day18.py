print("WELCOME TO THE GAME OF NUMBERS")

PUMA = 100000.26
attempt = 0

while True:
    print("You will Guess a number decimal points are allowed")
    boom=float(input("Enter a number between 10,000 and 1,000,000: "))
    
    if boom < 10000:
        print("Always try to follow instructions")
        exit()
    elif boom > PUMA:
        print("That's high you got to think of something lower")
        attempt +=1
    elif boom < PUMA:
        print("that's lower dude you got to think of something higher")
        attempt+=1
        continue
    elif boom == PUMA:
        print("That's a good shot, you won")    
        exit()
    else:
        print("What's that dude!")
          
    print("You have done this in" ,attempt,"attempts")
    if attempt == 5:
        print("The answer is", PUMA)
        exit()
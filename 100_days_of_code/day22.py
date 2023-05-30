import random

print("GAME OF RANDOMS")

puma = random.randint(10000,1000000)
attempt =0

while True:
    print("Game of numbers")
    boom=int(input("Enter the number you think the random number would be: "))
    
    if boom < puma:
        print("That's way too low mate!")
        attempt+=1
    elif boom == puma:
        print("That's correct Big man")
        exit()
    elif boom > puma:
        print("That's higher that what we thought of mate")
        attempt+=1
    else:
        print("That's not how we think here big man")
        
    print("That's like your", attempt,"attempt")
    if attempt == 5:
        print("Wow big man aren't you frustrated now. Here is the answer", puma)
        exit()
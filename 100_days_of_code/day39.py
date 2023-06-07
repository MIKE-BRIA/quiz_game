import random, os, time

words=["kenya","mexico","rwanda","panama","colombia","Riodejaneiro"]
picked=[]
lives=6

choseword=random.choice(words)

while True:
    time.sleep(1.1)
    os.system("clear")
    dwang=input("Choose a letter: ").strip().lower()
    
    if dwang in picked:
        print("You have done that before!")
        continue
    picked.append(dwang)
    
    if dwang in choseword:
        print("You found a word")
    else:
        print("Sorry about that you got no shit")
        lives-=1
        
    all=True
    print()
    for i in choseword:
        if i in picked:
            print(i, end="")
        else:
            print("_", end="")
            all=False
            
    print()
    
    if all:
        print(f"You won with {lives} left")
        break
    if lives<=0:
        print(f"You lost and the answer is {choseword}")
        break
    else:
        print(f"only {lives} left")
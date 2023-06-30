import os, time, random

def add():
    os.system("cls")
    idea=input("")
    f=open("my.ideas", "a+")
    f.write(f"{idea}\n")
    f.close()
    time.sleep(2)
    os.system("cls")

def show():
    os.system("cls")
    f=open("my.ideas", "r")
    ideas=f.read().split("\n")
    f.close
    ideas.remove("")
    idea=random.choice(ideas)
    print(idea)
    time.sleep(2)
    os.system("cls")

while True:
    print("Good time to store your ideas")
    print()
    menu= input("1: Add idea\n2: Show a random idea\n > ")
    if menu == "1":
        add()
    else:
        show()

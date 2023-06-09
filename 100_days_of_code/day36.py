names=[]

def pring():
    print()
    for i in names:
        print(i)
    print()

while True:
    first=input("What's your first name: ").strip().capitalize()
    last=input("What's your last name: ").strip().capitalize()
    name=f"{first} {last}"
    
    if name not in names:
        names.append(name)
    else:
        print("That is already present")
    pring
    
    
    
  
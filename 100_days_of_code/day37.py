print("STAR WARS NAME GENERATOR")

starwar=[]
def pring():
  for i in starwar:
    print(i)


while True:
  first=input("Enter your first name: ").strip().capitalize()
  last=input("Enter your last name: ").strip().capitalize()
  city=input("Enter the city where you were born: ").strip().capitalize()
  mum=input("Enter your Mum's maiden name: ").strip().capitalize()
  
  firs=(first[0:4])
  las=(last[0:3])
  mu=(mum[0:2])
  cit=(city[0:3])
  print()
  pull=f"{first} {last} {mum} {city}"
  print(pull)
  
  starr=f"{firs}{las} {mu}{cit}".title()
  if starr not in starwar:
    starwar.append(starr)
  else:
    print("We are not providing the same twice")

  print(f"Your Star Wars name is {starr}")
  print()
  pring()
import os,time, datetime
from replit import db

def add():
  os.system("clear")
  entry=input("What do you want to input:> ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key]=entry
  print("ADDED")
  time.sleep(2)
  os.system("clear")

def view():
  os.system("clear")
  keys = db.keys()
  for key in keys:
    print(f"""{key}
    {db[key]}""")
    opt=input("Next or Exit")
    if (opt.lower()[0]=="e"):
        break
  time.sleep(2)
  os.system("clear")

correctPassword="115371"
passwordEntered=input("Input password:>> ")
while True:
  print("This is a Private Diary")
  print()
  if passwordEntered == correctPassword:
    menu =input("1: ADD\n2: VIEW\n:>>> ")
    if menu == "1":
      add()
    else:
      view()
  else:
    print("ERROR")
    exit()

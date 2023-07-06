import time, os

list=[]
fileExists=True
try:
  f = open("calendar.txt","r") 
  myEvents = eval(f.read())
  f.close()
except:
  fileExists=False

def pring():
  print()
  for i in list:
    print(i)
    print()
    
def add():
  time.sleep(2)
  os.system("clear")
  adding=input("What do you want to add: ").capitalize()
  date=input("When is the task due: ").capitalize()
  prio=input("What's the priority  (high/medium/low): ").capitalize()
  
  addl=[[adding, date, prio]]
  list.append(addl)
  print("Added")
  #for i in addl:
    #list.append(addl)


def view():
  time.sleep(2)
  os.system("clear")
  vie=input("Do you want to (View all/ View priority): ").capitalize()
  if vie == "View all":
    for i in list:
      for t in i:
        print(t, end=" | ")
      print()
    print()
  else:
    boom=input("Which priority? ").capitalize()
    for i in list:
      if boom in i:
        for t in i:
          print(t, end=" | ")
        print()
      print()
    time.sleep(1)

def edit():
  time.sleep(2)
  os.system("clear")
  find=input("Which task do you want to edit? ")
  found= False
  for i in list:
    if find in i:
      found=True
  if not found:
    print("Couldn't find that")
    return
  for i in list:
    if find in i:
      list.remove(i)
  adding=input("Name > ")
  date=input("Date > ")
  prio=input("priority > ").capitalize()
  addl=[[adding, date, prio]]
  list.append(addl)
  print("Added")


def remove():
  time.sleep(2)
  os.system("clear")
  find=input("Name the task to remove: ")
  for i in list:
    if find in i:
      list.remove(i)


while True:
  print("Life Organizer")
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()


  time.sleep(1)
  os.system("clear")

  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass

  f = open("calender.txt", "w")
  f.write(str(list))
  f.close()
  
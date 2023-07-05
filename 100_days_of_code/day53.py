import os, time

mylist=[]

try:
  f=open("inventory.pbo", "r")
  mylist= eval(f.read())
  f.close()
except:
  print("file not found")

def add():
  time.sleep(2)
  os.system("clear")
  item=input("Input item to be added:> ")
  mylist.append(item)
  print("ADDED")
  
def view():
  time.sleep(1)
  os.system("clear")
  seen = []
  for item in mylist:
    if item not in seen:
      print(f"{item} {mylist.count(item)}")
      seen.append(item)

def remove():
  time.sleep(1)
  os.system("clear")
  rem=input("Input the item to remove:> ")
  for i in mylist:
    if rem in i:
      mylist.remove(i)
      print("DELETED")
      

while True:
  print("RPG Inventory")
  print()
  menu=input("1: Add\n2: Remove\n3: View\nchoose what you need:> ")
  if menu == "1":
    add()
  elif menu == "2":
    remove()
  else:
    view()

  f = open("inventory.pbo", "w")
  f.write(str(mylist))
  f.close()
  time.sleep(1)
  os.system("clear")
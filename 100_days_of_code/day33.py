def colorchange(color):
    if color=='red':
        return('\033[31m')
    elif color=='white':
        return('\033[0m')
    elif color=='blue':
        return('\033[34m')
    elif color=='yellow':
        return('\033[33m')
    elif color=='green':
        return('\033[32m')
    elif color=='purple':
        return('\033[35m')
      
title=f"{colorchange('purple')}TODO LIST MANAGER"
print(f"\t{title}")
print()

def pring():
  print()
  for i in list:
    print(i)
  print()
    
list=[]
while True:
  fun=input("Do you want to view, add or edit the todo list\n")
  fun=fun.lower()
  if fun == "view":
    pring()
  elif fun == "add":
    item=input("What do you want to do: ")
    list.append(item)
    pring()
  elif fun=="edit":
    item=input("Which task have you completed: ")
    if item in list:
      list.remove(item)
    else:
      print(f"{item} is not in the list")
    pring()
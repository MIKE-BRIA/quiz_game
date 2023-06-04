import os, time
list=[]

def pring():
  for i in list:
    print(i)
    
while True:
  title="EMAILING YEAP"
  print(title)
  print()

  option=input("What do you need\n 1:Add email\n 2:Remove email\n 3:Show email\n 4:Spam email\n Choose one:  ")

  if option == "1":
    email=input("Whats the email to add: ")
    list.append(email)
  elif option == "2":
    email=input("Whats the email to remove: ")
    if email in list:
      list.remove(email)
    else:
      print("Email not present")
  elif option=="4":
    email=input("Whats the email to spam: ")
    spam=f" Dear {email}\n It has come to our attention\n that you're missing out on\n the amazing chance\n to become one of\n the wealthiest men\n in this country becouse\n you do not want\n to invest with us"
    print(spam)
  elif option =="3":
    pring()
  time.sleep(2)
  os.system("clear")
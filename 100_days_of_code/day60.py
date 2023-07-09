import datetime, os, time

while True:
  today=datetime.date.today()
  print()
  print("Event countdown timer")
  print()

  event=input("Input the event:> ")
  year=int(input("Input the year:> "))
  month=int(input("Input the month:> "))
  day=int(input("Input the day:> "))

  even=datetime.date(year,month,day)
  
  diff = even - today
  diff=diff.days
  
  if even>today:
    print(event,"will be in",diff,"days")
  elif today>even:
    print(event,"has passed with",abs(diff),"days")
  else:
    print(event,"is taking place today")

  time.sleep(2)
  os.system("clear")
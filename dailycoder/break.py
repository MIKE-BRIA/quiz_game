answer = "My heart breaks"
answer = answer.lower()
attp = 1

while True:
  print("Fill in the blank space!")
  print("(Fill the blank to see if you know more than others)")
  boo=input("This world has broken me and now: ",)
  if boo == answer:
    print("Baby who hurt you")
  else:
    print("nop try again or haven't you gone through a heartbreak")
    attp += 1
  if boo == answer:
    break

print('thanks for playing')

print("you got the correct answer after", attp,"attempts")
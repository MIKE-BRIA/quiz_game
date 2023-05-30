print("WE WILL BE WORKING WITH THE MULTIPLICATION TABLE")

attempt=0
doo=int(input("Name your multiple: "))

for i in range(1,11):
    print(i,"X",doo)
    answer=int(input("What's your answer: "))
    ping=i*doo
    if answer == ping:
        print("That's correct dwang!")
        attempt+=1
    else:
        print("That's wrong, the correct answer is", ping)
if attempt == 10:
    print("You got all the answers correct you are the OG")
else:
    print("You scored",attempt,"out of 10")
    
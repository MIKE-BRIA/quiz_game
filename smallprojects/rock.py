print("welcome to the life game challenge")

playing = input("Are you sure you wanna play? ")
if playing.lower()!= "yes":
    quit()

print("okay lets play")
score=0
answer= input("what is the name of kenya capital city? ").lower()
if answer == "nairobi":
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input("where is the main port situated in Kenya? ").lower()
if answer == "mombasa":
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input("are kenyan ladies good at giving guys character development? ").lower()
if answer == "yes ":
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input("what is the most toxic county? ").lower()
if answer == "garrisa":
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input("which people consume a lot of fish? ").lower()
if answer == "luos":
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input("do you want to have a kenyan girlfriend when you are still broke? ").lower()
if answer == "no":
    print('correct!')
    score +=1
else:
    print('incorrect!')
    
print("you got" + str(score) + "questions correct")
print("you got" + str((score/6)*100)+"%")

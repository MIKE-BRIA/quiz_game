import os, time

while True:

    print("HIGH SCORE TABLE")
    print()
    f=open("high.score", "a+")
    dwing=input("What are the Initials? ").upper()
    dwang=input("What are the scores? ")

    f.write(f"{dwing}  {dwang}\n")
    f.close()

    print("ADDED")
    time.sleep(1)
    os.system("clear")
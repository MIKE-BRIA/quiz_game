import os
import datetime
import time
from replit import db

def add():
    tweet = input("What's your tweet: ")
    timestamp = datetime.datetime.now()
    key = f"mes{timestamp}"
    db[key] = tweet
    print("ADDED")
    time.sleep(1)
    os.system("clear")

def view():
    os.system("clear")
    keys = db.keys()
    for key in keys:
        print(f"{key}: {db[key]}")
    time.sleep(2)
    os.system("clear")

while True:
    print("Tweets center")
    print()
    menu = input("1: Add Tweet\n2: View Tweet\n>>> ")
    if menu == "1":
        add()
    else:
        view()






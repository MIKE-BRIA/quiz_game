import os, time

while True:
    time.sleep(2)
    os.system("clear")
    
    print("ALL THINGS ABOUT WEBSITES")
    print()
    name=input("What's the name of your website: ")
    url=input("What's the url of your website: ")
    desc=input("How can your describe your website: ")
    rating=input("What's the rating of your website: ")
    
    website={"Name": name, "Url": url, "Desc": desc, "Rate": rating}
    
    for key, values in website.items():
        print(f"{key} {values}")
    
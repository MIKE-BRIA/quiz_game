import os, time

while True:
    time.sleep(2)
    os.system("clear")

    print("Contact Card")
    name=input("Input your name: ")
    date=input("input your date of birth: ")
    number=input("Input your phone number: ")
    email=input("Input your email: ")
    address=input("Input your Address: ")

    details={"Name": name, "Dob": date, "number": number, "email": email, "address": address}

    print()
    print(f"""Name: {details["Name"]}""")
    print(f"""DOB: {details["Dob"]}""")
    print(f"""Tel: {details["number"]}""")
    print(f"""Email: {details["email"]}""")
    print(f"""Address: {details["address"]}""")
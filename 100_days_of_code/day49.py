f=open("high.score", "r")

while True:
    contents=f.readline().split()
    print(contents)

    if contents=="":
        break

f.close()
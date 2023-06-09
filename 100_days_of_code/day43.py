import random

bing=[]

def ran():
  number=random.randint(1,99)
  return number

def prettyprint():
  for i in bing:
    print(i)

numbers=[]
for i in range(9):
  numbers.append(ran())

numbers.sort()
print(" Deric's Nan's Bingo Generator")
bing=[[numbers[0], numbers[1], numbers[2]],
      [numbers[3], "BINGO", numbers[4]],
      [numbers[5], numbers[6], numbers[7]]
     ]

prettyprint()
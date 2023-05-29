amount = 10000
interest=0.07

for i in range (5):
    amount+=(amount*interest)
    print("Year", i+1, "amounted to", amount)
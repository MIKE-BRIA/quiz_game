counts = dict()
line=input("Enter a line of text: ")
words= line.split()

print(words)

# counting the most repeated word

print("counting word")

for i in words:
    counts[i]=counts.get(i,0)+1
print(i)
print(counts)
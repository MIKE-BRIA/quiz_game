print("You have managed lets hear your thoughts")

for i in range(1,31):
    print(f"Day {i: ^2}:")
    thought=input("what do you think about this day: ")
    output=f"You thought Day {i: ^2} was {thought}"
    print()
    print(f"{output: ^60}")
"""for i in range(5):
    print("*", end="")"""

for i in range(5):
    for j in range(0, 6 - i):
        print(" ", end=" ")
    print(("*" * ((2 * i) + 1)))

from numpy import sort

a = int(input("Enter a number:"))
b = []
for i in range(1, a + 1):
    b.append(int(input(f"enter a element: {i}:")))
print(sort(b))
"""for i in range(a):
    for j in range(i + 1, a):
        if a[i] > b[j]:
            c = b[i]
            b[i] = b[j]
            b[j] = c"""
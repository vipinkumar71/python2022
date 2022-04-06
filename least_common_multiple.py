def least_common_multiple(a, b):
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b):
            lcm = greater
            break
        greater = greater + 1
    return lcm


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(least_common_multiple(a, b))

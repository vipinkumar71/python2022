a = int(input("enter a number:"))
number1 = 0
number2 = 1
counting = 0
if a == 0:
    print("result is not possible")
elif a == 1:
    print(a)
else:
    print("fibonacci series")
    while counting < a:
        print(number1)
        result = number1 + number2
        number1 = number2
        number2 = result
        if number1 >= a:
            break

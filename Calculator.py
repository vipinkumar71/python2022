
def add(n1, n2):
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def substraction(n1, n2):
    return n1 - n2


def reminder(n1, n2):
    return n1 % n2


def calculator(op, n1, n2):
    if op == "+":
        print(f"addition:{add(int(n1), int(n2))}")
    elif op == "*":
        print(f"multiplication:{multiplication(int(n1), int(n2))}")

    elif op == "/":
        print(f"divide:{divide(int(n1), int(n2))}")

    elif op == "-":
        print(f"subtraction:{substraction(int(n1), int(n2))}")
    elif op == "%":
        print(f"reminder:{reminder(int(n1), int(n2))}")


def get_input():
    op = input("Enter operator:")
    n1 = input("Enter first number:")
    n2 = input("Enter second number:")
    calculator(op, n1, n2)


get_input()


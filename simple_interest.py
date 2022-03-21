p = int(input("Principal amount:"))
t = int(input("Time period:"))
r = int(input("Rate of interest:"))


def simple_interest(p, t, r):
    print("The initial principal is", p)
    print("The time period is ", t)
    print("The rate of interest is", r)
    si = (p * t * r) / 100
    print("The simple interest is", si)
    # Here A is the total amount
    A = si + p
    print("The total amount is", A)
    return si
    return A


simple_interest(1000000, 1, 7)


def compound_interest(p, r, t):
    Amount = p * (pow((1 + r / 1000), t))
    ci = Amount - p
    print("compound interest is ", ci)
    return ci


compound_interest(p, r, t)

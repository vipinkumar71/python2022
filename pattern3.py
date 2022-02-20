# like a Christmas but upside down tree
"""for i in range(10, 0, -1):
    print(" " * (10 - i) + "* " * i)"""

# like a Christmas tree
"""for i in range(1, 10):
    print(" " * (10 - i) + "* " * (i))"""
# Christmas tree with= (2n+1)
for i in range(0, 6):
    for j in range(0, 6 - i):
        print("  ", end="")
    print("* " * ((2 * i) + 1))

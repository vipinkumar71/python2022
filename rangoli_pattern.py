n = int(input())


def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size - 1, -size, -1):
        temp = '-'.join(alp[size - 1:abs(i):-1] + alp[abs(i):size])
        print(temp.center(4 * size - 3, '-'))


print_rangoli(n)

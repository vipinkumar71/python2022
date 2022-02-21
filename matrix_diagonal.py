from random import choice

a = [x for x in range(10)]
n = int(input("Enter the Number:"))
matrix = [[choice(a) for i in range(n)] for j in range(n)]
print(matrix)

if n % 2 != 0:
    med = int((n - (n / 2) - 1))
    r_value = matrix[med][med]
    for i in range(n):
        matrix[i][i] = r_value

if n % 2 == 0:
    med = int((n - (n / 2)) - 1)
    med2 = med + 1
    r_value = matrix[med][med] if matrix[med][med] > matrix[med2][med2] else matrix[med2][med2]
    for i in range(n):
        matrix[i][i] = r_value
print(matrix)

score = 0
vowels = "aeiou"
for i in range(10):
    value = input()
    if value in vowels:
        score += 10
    else:
        score -= -2
print(score)

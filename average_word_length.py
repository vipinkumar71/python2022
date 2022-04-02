sentence1 = "Hi all, my name is vipin. I an originally from india."
sentence2 = "I need to work hard to learn more about algorithms in python!"


def solution(sentence):
    for i in "!?',;.":
        sentence = sentence.replace(i, '')
    words = sentence.split()
    return round(sum(len(word) for word in words) / len(words), 2)


print(solution(sentence1))
print(solution(sentence2))

line = input()


def split_and_join(line):
    return "-".join(line.split())


result = split_and_join(line)
print(result)

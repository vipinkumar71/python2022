a = {("key1", "key2"): [(1, 2, 3)], "value": ["This is world", ("Hello", "fun")]}

print(list(a.keys())[1])
# value
print(list(a.values())[1][1][1])
#fun

a = {}
l = int(input("Length of dict:"))

for i in range(l):
    key = input("Enter key:")
    value = input("Enter Value:")
    type_of_value = input("Enter type of value:")
    if type_of_value == int:
        value = int(value)
    else:
        pass
    a.update({key: value})
print(a)

for k, v in a.items():
    if type(v) == str:
        if v.isnumeric():
            a.update({k: int(v)})
print(a)

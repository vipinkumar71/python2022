n = int(input("enter a n value:"))  # How many keys:values pair you want
d = {}  # Empty dictionary

for i in range(n):  # By using the for loop
    keys = input()  # input for keys in string
    values = input()  # input for values in string
    if keys.isalpha():  # if the value in keys is alphabet then pass because it is already in str
        pass
    else:
        keys = int(keys)  # if the value in keys is numeric then convert the keys type into integer

    if values.isalpha():  # if the values is alphabet then pass because it is already in str
        pass
    else:
        values = int(values)  # if the values is numeric then convert the values into integer by using casting

    d.update({keys: values}) # d[keys]=values
print(d)

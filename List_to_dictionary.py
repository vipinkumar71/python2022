a = ["name", "vipin", "age", 29, "city", "Shimla", "id", 40, "state", "Hp"]
b = {}
for i in a:
    if a.index(i) % 2 == 0:
        b.update({i: a[a.index(i) + 1]})
print(b)

"""a=["name","vipin","id","34","city","kullu"]
b={}
for i in range (0,len(a),2):
    b.update({a[i]:a[i+1]})
print(b)"""

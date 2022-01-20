a=["name","vipin","id","34","city","kullu"]
b={}
for i in range (0,len(a),2):
    b.update({a[i]:a[i+1]})
print(b)
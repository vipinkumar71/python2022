a=[3,2,4,6,8,12]
temp=0
for i in  range(len(a)):
 for j in range(i+1,len(a)): 
  if a[i]>a[j]:
   temp,a[i],a[j]=a[i],a[j],a[temp]
print(a)

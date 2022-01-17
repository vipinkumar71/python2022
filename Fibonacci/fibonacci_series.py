a=24
f_list=[]
for i in range(24):
 if len(f_list)<2:
  f_list.append(0)
  f_list.append(1)
 else:
  f_list.append(f_list[-1]+f_list[-2])
print(f_list)

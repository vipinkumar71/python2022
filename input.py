a= input("write a word:")
v="aeiou"
vowels=0
consonant=0
for i in a:
 if i in v:
  vowels +=1
 else:
  consonant +=1

print("vowels=",vowels)
print("consonant=", consonant)

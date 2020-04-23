string = input()
u,l = 0,0
for i in string:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("UPPER CASE",u)
print("LOWER CASE",l)
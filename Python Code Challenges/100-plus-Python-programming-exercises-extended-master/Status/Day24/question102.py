s = input()
d=l=0
for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1

print("Digits - ", d)
print("Letters - ", l)
string = input()
letter = 0
digit = 0
for i in string:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        letter+=1
print("LETTERS",letter)
print("DIGIT",digit)
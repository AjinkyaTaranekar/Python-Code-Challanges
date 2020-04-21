res=""
while(True):
    string = input()
    if string:
        res+=string.upper()+"\n"
    else:
        break
print(res)
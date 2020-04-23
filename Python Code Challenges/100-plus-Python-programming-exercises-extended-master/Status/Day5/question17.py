transaction = []
while(True):
    trans = list(map(str,input().split()))
    if trans:
        transaction.append(trans)
    else:
        break
total = 0
for i in transaction:
    if i[0] == 'D':
        total+=int(i[1])
    else:
        total-=int(i[1])
print(total)
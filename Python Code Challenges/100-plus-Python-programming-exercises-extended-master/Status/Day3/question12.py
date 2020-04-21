res = []
for i in range(2000,3000,2):
    i = str(i)
    if int(i[1])%2==0 and int(i[2])%2==0:
        res.append(i)
print(",".join(res))
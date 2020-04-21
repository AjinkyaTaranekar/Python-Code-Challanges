num = list(map(str,input().split(",")))
res=[]
for i in num:
    if int(i,2)%5==0:
        res.append(i)
print(",".join(res))
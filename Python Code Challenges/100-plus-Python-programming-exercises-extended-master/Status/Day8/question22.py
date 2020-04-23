import operator

string = list(map(str,input().split()))
res = dict()
for i in string:
    if i in res:
        res[i]+=1
    else:
        res[i]=1

res = sorted(res.items(), key = operator.itemgetter(0))
for i in res:
    print(i[0],":",i[1],sep="")
t=(1,2,3,4,5,6,7,8,9,10)
l=list()
for i in t:
	if t[i]%2==0:
		l.append(t[i])
t=tuple(l)
print (t)
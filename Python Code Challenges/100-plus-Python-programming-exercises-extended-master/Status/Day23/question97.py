import string
from collections import defaultdict

d = defaultdict(list)
num = input()
alph = list(string.ascii_lowercase)

for i in range(1,(2*num-1)+1):
	for j in range(1,(2*(2*num-1)-1)+1):
		d[i].append('-')

k = (len(d)*2)//2
temp = (len(d)//2 )
for i in range(1,len(d)+1):
	if i <= (len(d)+1)//2:
		index = num
		middle  = (len(d[i])+1)//2
		for j in range(k,k+4*i-3,2):
			d[i][j-1] = alph[index-1]
			if j >= middle:
				index = index +1
			else:
				index = index -1
		k = k-2
	else:
		d[i] = d[temp]
		temp = temp -1
		
# print d

for i in range(1,len(d)+1):
	print (''.join(d[i]))
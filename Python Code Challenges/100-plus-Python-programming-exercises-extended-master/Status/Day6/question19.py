from operator import itemgetter

personInfo = []

while True:
	line = input()
	if not line:
		break
	personInfo.append(tuple(line.split(',')))

personInfo = sorted(personInfo, key=itemgetter(0,1,2))
print(personInfo)
directionInfo = []

while True:
	line = input()
	if not line:
		break
	directionInfo.append(tuple(line.split()))

x,y = 0,0
for i in directionInfo:
    if i[0] == "UP":
        x+=int(i[1])
    if i[0] == "DOWN":
        x-=int(i[1])
    if i[0] == "LEFT":
        y-=int(i[1])
    if i[0] == "RIGHT":
        y+=int(i[1])

print(int((x*x+y*y)**0.5))
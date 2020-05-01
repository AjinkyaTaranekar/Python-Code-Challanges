import math
def binarySearch(l, element):
    bottom = 0
    top = len(l)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if l[mid]==element:
            index = mid
        elif l[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

l=[0,5,8,9,12,17,22,52]
print (binarySearch(l,11))
print (binarySearch(l,12))
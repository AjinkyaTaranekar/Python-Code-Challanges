m = int(input())
M = set(map(int,input().split()))

n = int(input())
N = set(map(int,input().split()))

res = (M.difference(N)).union(N.difference(M))

for i in sorted(list(res)):
        print (i)
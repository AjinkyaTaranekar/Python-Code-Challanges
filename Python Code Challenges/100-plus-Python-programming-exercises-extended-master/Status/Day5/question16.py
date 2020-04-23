nums = list(map(int,input().split(",")))
print(",".join([str(i*i) for i in nums if i % 2!=0]))

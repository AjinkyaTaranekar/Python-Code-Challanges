def maxStr(a,b):
    return  max([a,b],key = len) if len(a)!=len(b) else a+'\n'+b
a,b = map(str,input().split())
print(maxStr(a,b))
import re
def validate(pwd):
    res = []
    for p in pwd:
        if len(p)>=6 and len(p)<=12 and re.search("[a-z]",p) and re.search("[0-9]",p) and re.search("[$#@]",p) and re.search("[A-Z]",p):
            res.append(p)
    return res

pwd = list(map(str,input().split(",")))
res = validate(pwd)
print(",".join(res))
import re
emailAddress = input()
check = "(\w+)@((\w+\.)+(com))"
r2 = re.match(check,emailAddress)
print (r2.group(1))
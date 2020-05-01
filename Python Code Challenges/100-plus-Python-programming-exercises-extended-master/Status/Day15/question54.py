import re
emailAddress = input()
check = "(\w+)@(\w+)\.(com)"
r = re.match(check,emailAddress)
print (r.group(2))
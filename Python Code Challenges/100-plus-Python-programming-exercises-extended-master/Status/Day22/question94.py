def solve(heads,legs):
    ns='No solutions!'
    for i in range(heads+1):
        j=heads-i
        if 2*i+4*j==legs:
            return i,j
    return ns,ns

heads=35
legs=94
solutions=solve(heads,legs)
print (solutions)
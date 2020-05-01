def prCharWithFreq(str): 
  
    d = {} 
    for i in str: 
        if i in d: 
            d[i] += 1
        else: 
            d[i] = 1
    
    for i in sorted(d.values()): 
        print("{} {}".format(i,d[i]), end ="\n") 
        
str = input() 
prCharWithFreq(str) 
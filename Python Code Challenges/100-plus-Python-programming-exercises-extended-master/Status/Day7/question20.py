class GenerateNumbersDivisibleBy7():
    def __init__(self):
        self.n = 0

    def getNum(self):
        self.n = int(input())
        
    def printString(self):
        print(",".join([str(i) for i in range(self.n) if i%7==0]))

n = GenerateNumbersDivisibleBy7()
n.getNum()
n.printString() 

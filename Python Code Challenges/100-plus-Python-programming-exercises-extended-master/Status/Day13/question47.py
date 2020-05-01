import math
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*math.pi

aCircle = Circle(3)
print (aCircle.area())
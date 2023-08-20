#half done
import math
class shape:
    pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius 
    
    def vol(self):
        return math.pi*radius

d1=shape()
c1=circle(10)
print(c1)
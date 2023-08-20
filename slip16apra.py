class rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid

    def area(self):
        return self.len*self.wid
    
    def perimeter(self):
        return 2*(self.len+self.wid)*self.len*self.wid
    
d1=rectangle(3,3)
print(d1.area())
print(d1.perimeter())

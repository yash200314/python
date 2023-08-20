class Rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid

    def area(self):
        return self.len*self.wid
    
    def peri(self):
        return 2*(self.len+self.wid)


d=Rectangle(2,8)

print(d.area())
print(d.peri())
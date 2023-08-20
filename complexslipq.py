class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    
    def __add__(self,other):
        return complex(self.real+other.real,self.imaginary+other.imaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}"

d1=complex(2,5)
d2=complex(3,5)
c3=d1+d2
print(c3)


class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,other):
        return complex(self.real+other.real,self.imaginary+other.imaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=complex(6,8)
c2=complex(8,7)
c3=c1+c2
print(c3)
class Employee:
    def accept(self):
        self.name=input("Enter the name:")
        self.sal=int(input("Enter the salary:"))
        self.age=int(input("Enter the age:"))

    def display(self):
        return "f Name is{self.name}.Salary is:{self.sal}.Age{self.age}"
    
    def __add__(self,other):
        return(self.sal+other.sal)

d1=Employee()
d2=Employee()

d1.accept()
d2.accept()

d1.display()
d2.display()
print(d1+d1)

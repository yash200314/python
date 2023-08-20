class cal:
   # def __init__(self,name,age):
    #    self.name=name
    #    self.age=age

    def __add__(self,name,age):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))

    def display(self,name,age):
        print("name is:",self.name)
        print("age is:",self.age)

d1=cal()
d1.__add__("yash",19)
d1.display("yash",10)
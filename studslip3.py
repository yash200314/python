class student:
    def __init__(self,roll,name,age,gender):
        self.roll=roll
        self.name=name
        self.age=age
        self.gender=gender

class test(student):
    def __init__(self,roll,name,age,gender,sub1,sub2,sub3):
        super().__init__(roll,name,age,gender)
        self.mark1=sub1
        self.mark2=sub2
        self.mark3=sub3

    def getmarks(self):
        self.total=self.mark1+self.mark2+self.mark3
        print(self.name,"\b's marks:",self.total)
        print("sub1 marks:",self.mark1)
        print("sub2 marks:",self.mark2)
        print("sub3 marks:",self.mark3)

p1=test(1,"yash",19,"male",89,90,90)
p2=test(2,"roy",31,"male",12,23,12)
p1.getmarks()
p2.getmarks()

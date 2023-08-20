# class Emp:
#     def __init__(self ,id,name,department,salary):
#         self.id=id
#         self.name=name
#         self.department=department
#         self.salary=salary

#     def accept(self):
#         self.id=int(input("Enter the id:"))
#         self.name=input("Enter the name:")
#         self.department=input("Enter the department:")
#         self.salary=int(input("Enter the salary"))
    
#     def display(Self):
#         print("id---->",self.id)
#         print("name---->",self.name)
#         print("department----->",self.department)
#         print("salary---->",self.salary)

# class Manager(Emp):
#     def __init__(self ,id,name,department,salary,bonus):
#         super().__init__(id, name, department, salary)
#         self.bonus=bonus

#     def accept(self):
#         super().accept()
#         self.bonus=float(input("Enter the bonus:"))

#     def display(self):
#         super().display()
#         print(f"bonus:{self.bonus}")
    

# n = int(input("Enter number of managers: "))
# man = []
# for i in range(n):
#     print("Enter the details of manager:")
#     m=Manager(None,None,None,None,None)
#     m.accept()
#     man.append(Manager)

# msal=-1
# msalman=None
# for Manager in man:
#     tsal=msal.manager.bonus
#     if tsal>msal:
#         maxsal=tsal
#         msalman=Manager

class Emp:
    def __init__(self,id,name,department,sal):
        self.id=id
        self.name=name
        self.department=department
        self.sal=sal

class manager(Emp):
    def __init__(self,id,name,department,sal,bonus):
        super(manager,self).__init__(id,name,department,sal)
        self.bonus=bonus

    def totalsal(self):
        print(self.name,"sal got:",self.sal+self.bonus)


m1=manager(1,"yash","general",2000,200)
m2=manager(2,"roy","hod",1000,10)
m1.totalsal()
m2.totalsal()
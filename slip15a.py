class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    

student=student("yash",90)

#original marks
print("original name is:",student.name)
print("original marks is:",student.marks)

#modify
student.name="roy"
student.marks=89

print("modified name is:",student.name)
print("modified marks is:",student.marks)
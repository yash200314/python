class demo(Exception):
    def __init__(self,message="age not valid"):
        super().__init__(self,message)

try:
    n=int(input("Enter the age:"))

    if n<18:
        raise demo
    else:
        print("you can vote")

except demo:
    print("invalid age !!")
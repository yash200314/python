class demo(Exception):
    def __init__(self, message="invalid number"):
       super().__init__(self,message)

try:
    n=int(input("Enter the number:"))
    if n>-1:
        print("positive integer")
    if n<0:
        raise demo
except demo:
    print("invalid number!!!")
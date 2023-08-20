class demo(Exception):
    def __init__(self,message):
        super().__init__(self,message)

try:
    n=int(input("Enter the age"))

    if n<18:
        raise demo

except demo:
    print("Lodu you cannot vote!!!!")
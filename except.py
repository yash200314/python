class demo(Exception):
    def __init__(self,message="string found!!!!"):
        super().__init__(self,message)

try:
    n=input("Enter the string:")

    print(n)

    if n.isnumeric():
        print("it is not a string")
    else:
        raise demo


except demo:
    print("It is a String !!!!")
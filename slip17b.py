class demo(Exception):
    def __init__(self,message="Invalid date!!!"):
        super().__init__(self,message)

try:
    date=int(input("Enter the date:"))
    month=int(input("Enter the month:"))
    year=int(input("Enter the year"))

    if date>31:
        raise demo
    if month>12:
        raise demo
    if year<0:
        raise demo

except demo:
    print("invalid date!!!!!!!")
    

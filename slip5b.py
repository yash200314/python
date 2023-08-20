#WriteapythonscripttogenerateFibonaccitermsusinggenerator
#function
def generator(r):
    a=0;b=1
    for i in range(1,r):
        print(b)
        a,b=b,a+b
n=int(input("enter the number:"))
if n==0:
    print(0)
else:
    print(0)
    generator(n)
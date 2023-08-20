str=input("Enter the string")
x=list(str)
for i in range(len(str)):
    if i%2!=0:
        x.remove(str[i])
        print(str)
print(x)
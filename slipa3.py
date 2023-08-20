dict={}
n=int(input("Enter the number of keys:"))
for i in range(n):
    key=int(input("Enter the key:"))
    if key in dict:
        print("the key already exist:")

    for key in dict.keys():
        print(key,end="")
    print("use another keys:")
    key=int(input("Enter the value:"))

    value=0
    dict[key]=value
    print(dict)

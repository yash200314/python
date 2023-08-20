list=[]
n=int(input("Enter the number:"))
for i in range(n):
    value=int(input())
    list.append(value)
print(list)
new_list=[]
for x in list:
    if x not in new_list:
        new_list.append(x)
    print(new_list)


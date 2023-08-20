#accept a number and remove a duplicate number from it
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
        print(x)
    
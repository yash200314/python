dict={}
str=input("enter the string")
for i in str:
    cnt=0
    for j in range(len(str)):
        if i==str[j]:
            cnt=cnt+1
    if cnt>=1:
        dict[i]=cnt
print(dict)

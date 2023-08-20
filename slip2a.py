n=input("Enter the string:")
# accepting the string
low=up=ele=0
#initialize the element to zero
for i in n:
    if i.isupper():# use of inbuilt function
        up=up+1
    if i.islower():
        low=low+1
    else:
        ele=ele+1
print("No. of uppercase is ",up)
print("No of lowercase element is:",low)
print("No of other element is:",ele)

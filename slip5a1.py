n=input("Enter the string:")
low=up=ele=0
for i in n:
    if i.isupper():
        up=up+1
    if i.islower():
        low=low+1
    else:
        ele=ele+1

print("No. of uppercase character:--",up)
print("No. of lowercase character:--",low)
print("other special symbol",ele)


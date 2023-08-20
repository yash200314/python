dictionary={};
n=int(input("enter the value"));
for i in range (0,n):
    key=input("enter the number");
    value=input("enter the number");
    dictionary[key]=value;
    print(dictionary);
    
search=int(input("enter the value to be searched"));
if search in dictionary:
    print("value is present");
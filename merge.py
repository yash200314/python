dictionary={};
dictionary1={};
num=int(input("enter the number"));
for i in range(0,num):
    key=input("enter the number");
    value=input("enter the number");

    dictionary[key]=value;
    print(dictionary);
num1=int(input("enter the n"))
for i in range(0,num1):
    key1=input("enter the number");
    value1=input("enter the number");

    dictionary[key1]=value1;
    print(dictionary1);
    dictionary.update(dictionary1);

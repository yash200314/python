str=input("enter the string:\n");
odd="remove odd character"
for i in range(len(str)):
    if i % 2 !=0:   
        odd=str[i];
        print("the odd value are as follows",odd);
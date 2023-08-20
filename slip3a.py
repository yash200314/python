#check if a given key exist in a dictionary if key present replace it
dictionary={}
n=int(input("Enter the number of keys:--"))
for x in range(0,n):
    key=input("Enter the key:--")
    if key in dictionary:
        print("the key exist")

        for key in dictionary.keys():
            print(key,end='')
        print("\n use differnt key:")
        key=input("enter the key:")
        value=input("enter the value:")
        dictionary[key]=value
        print(dictionary)
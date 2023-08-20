tuple=(1,2,2,3,4,4,3,2,3,5)
repeated=[]
for item in tuple:
    if tuple.count(item)>1 and item not in repeated:
        repeated.append(item)
print(repeated)
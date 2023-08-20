dict={"apple":10,"banana":69,"cherry":87}
key_replace="banana"
new_value="mango"
new_key=78
if key_replace in dict:
    dict[new_key]=new_value
    del dict[key_replace]
print(dict)